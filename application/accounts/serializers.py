from django.utils import timezone
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.models import make_password, User
from application.accounts.tasks import (
    send_confirmation_email, send_confirmation_email_mentor,
    send_password_recovery
)

User = get_user_model()


class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(
        min_length=6,
        write_only=True,
        required=True
    )
    
    class Meta:
        model = User
        fields = [
            "email", "password", "password_confirm", "first_name", "last_name"
        ]
        
    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        
        if password != password_confirm:
            raise serializers.ValidationError("Пароли не совпадают.")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email.delay(user.email, code)
        return user
    

class TeacherRegisterSerializer(serializers.ModelSerializer):
    experience = serializers.CharField(min_length=6, required=True)
    audience = serializers.CharField(min_length=6, required=True)
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(
        min_length=6,
        write_only=True,
        required=True
    )
    
    class Meta:
        model = User
        fields = [
            "email", "password", "password_confirm", 
            "first_name", "last_name", 
            "experience", "audience"
        ]
        
    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        
        if password != password_confirm:
            raise serializers.ValidationError("Пароли не совпадают.")
    
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email_mentor.delay(user.email, code)
        return user
        

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)
    
    def validate(self, attrs):
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.get("new_password_confirm")
        
        if new_password != new_password_confirm:
            raise serializers.ValidationError("Пароли не совпадают.")
        return attrs
    
    def validate_old_password(self, old_password):
        request = self.context.get("request")
        user = request.user
        if not user.check_password(old_password):
            raise serializers.ValidationError("Не верный пароль.")
        return old_password
    
    def set_new_password(self):
        user = self.context.get("request").user
        password = self.validated_data.get("new_password")
        user.password = make_password(password)
        user.save()
        
        
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    
    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Такого пользователя не существует.")
        return email
    
    def send_code(self):
        email = self.validated_data.get("email")
        user = User.objects.get(email=email)
        user.password_requested = timezone.now()
        user.create_activation_code()
        user.create_recovery_code()
        user.save()
        send_password_recovery.delay(email, user.activation_code, user.confirmation_code)
        user.activation_code = ""
        

class ForgotPasswordConfirmSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    recovery_code = serializers.CharField(required=True)
    password = serializers.CharField(min_length=6, required=True)
    password_confirm = serializers.CharField(min_length=6, required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Такого пользователя не существует.")
        return email

    @staticmethod
    def validate_code(code):
        if not User.objects.filter(confirmation_code=recovery_code).exists():
            raise serializers.ValidationError("Код введен не правильно!")

    def validate(self, attrs):
        password = attrs.get("new_password")
        password_confirm = attrs.get("new_password_confirm")
        
        request_time = timezone.now() - user.password_requested
        if request_time.total_seconds() > 24 * 60 * 60:
            raise serializers.ValidationError("Ссылка просрочена, пожалуйста сделайте новый запрос.")
        
        if password != password_confirm:
            raise serializers.ValidationError("Пароли не совпадают.")
        return attrs
    
    def set_new_password(self):
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        user = User.objects.get(email=email)
        user.password = make_password(password)
        user.save()