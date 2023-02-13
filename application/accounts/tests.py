from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

User = get_user_model()


class AccountTest(APITestCase):
    @property
    def example_bearer_token(self):
        """ Функция для получения токена. """
        user = User.objects.create_user(
            email="example@mail.com",
            password="qwerty",
            is_active=True,
        )
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    
    def test_create_student_account(self):
        """ Тест на регистрацию студентов. """
        
        url = "http://127.0.0.1:8000/api/v1/accounts/register/student/"
        response = self.client.post(url, data={
                "email": "example@mail.com",
                "first_name": "Cid",
                "last_name": "Kageno",
                "password": "qwerty",
                "password_confirm": "qwerty"
            }
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, 
            "Error. Please check email, password or first name and last name."
        )
    
    def test_create_teacher_account(self):
        """ Тест на регистрацию менторов. """
        
        url = "http://127.0.0.1:8000/api/v1/accounts/register/teacher/"
        response = self.client.post(url, data={
                "email": "exapmle@mail.ru",
                "first_name": "Sid",
                "last_name": "Kageno",
                "password": "qwerty",
                "password_confirm": "qwerty",
                "experience": "онлайн",
                "audience": "в настоящий момент нет"
            }
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED,
            "Error. Please check email, password or first name and last_name." 
        )
        
    def test_login_account(self):
        """ Тест на авторизацию пользователей. """
        
        url = "http://127.0.0.1:8000/api/v1/accounts/login/"
        user = User.objects.create_user(
            email="example@mail.com",
            password="qwerty",
            is_active=True
        )
        response = self.client.post(url, data={
                "email": "example@mail.com",
                "password": "qwerty",
            }
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            "Error. Please check email or password."
        )
        
    def test_change_password(self):
        """ Тест на смену пароля пользователей. """
        
        url = "http://127.0.0.1:8000/api/v1/accounts/change_password/"
        response = self.client.post(url, data={
                "old_password": "qwerty",
                "new_password": "qwerty12",
                "new_password_confirm": "qwerty12",
            },
        **self.example_bearer_token
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            "Error. Please check passwords."    
        )
        
    def test_forgot_password(self):
        """ Тест на восстановление пароля, отправка сообщения на почту. """
        
        url = "http://127.0.0.1:8000/api/v1/accounts/forgot_password/"
        user = User.objects.create_user(
            #? При создании пользователя чтобы получить письмо в тесте, укажите рабочую почту.
            email="nsabyrkulov@list.ru",
            password="qwerty",
            is_active=True,
        )
        response = self.client.post(url, data={
                "email": "nsabyrkulov@list.ru"
            },
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            "Error. Something get wrong. That's not developer fault."
        )