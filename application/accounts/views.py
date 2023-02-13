from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from application.accounts.serializers import (
    StudentRegisterSerializer, TeacherRegisterSerializer, ChangePasswordSerializer,
    ForgotPasswordConfirmSerializer, ForgotPasswordSerializer
)

User = get_user_model()


class StudentRegisterAPIView(APIView):
    def post(self, request):
        serializer = StudentRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            "Вы успешно зарегистрировались."
            " Мы отправили письмо с активацией профиля на вашу почту.",
            status=status.HTTP_201_CREATED
        )


class TeacherRegisterAPIView(APIView):
    def post(self, request):
        serializer = TeacherRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            "Вы успешно зарегистрировались."
            " Мы отправили письмо с активацией профиля на вашу почту.",
            status=status.HTTP_201_CREATED
        )
        

class MentorActivationAPIView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.is_mentor = True
            user.activation_code = ""
            user.save()
            return Response(
                {"Message": "successfully"},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"Message": "wrong email"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
            
class StudentActivationAPIView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ""
            user.save()
            return Response(
                {"Message": "seccessfully"},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"Message": "wrong email"},
                status=status.HTTP_400_BAD_REQUEST
            )
    

class ChangePasswordAPIView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response(
            "Пароль успешно обновлен.",
            status=status.HTTP_200_OK
        )
        
    
class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response("Мы выслали ссылку для сброса пароля.")

        
class SetNewPasswordAPIView(APIView):
    def post(self, request, activation_code):
        user = User.objects.get(activation_code=activation_code)
        serializer = ForgotPasswordConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response(
            "Пароль успешно обновлен.",
            status=status.HTTP_200_OK
        )