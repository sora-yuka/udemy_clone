from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("first_name", "admin")
        extra_fields.setdefault("last_name", "super_user")
        extra_fields.setdefault("role", "Admin")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=155)
    first_name = models.CharField(max_length=85)
    last_name = models.CharField(max_length=85)
    experience = models.CharField(max_length=85, blank=True)
    audience = models.CharField(max_length=85, blank=True)
    is_active = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=155, blank=True)
    confirmation_code = models.CharField(max_length=8, blank=True)
    password_requested = models.DateTimeField(null=True, blank=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
        
    def create_recovery_code(self):
        from random import randint
        recovery_code = randint(000_000, 999_999)
        self.confirmation_code = recovery_code
