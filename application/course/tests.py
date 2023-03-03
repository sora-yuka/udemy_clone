from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from application.course.models import Category

User = get_user_model()

class CourseTest(APITestCase):
    
    
    @property
    def bearer_token(self):
        """ Функция для получения токена. """
        user = User.objects.create_user(
            email="example@gmail.com",
            password="qwerty",
            is_active=True
        )
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
    
    
    def test_create_course(self):
        """ Тест на создание курса. """
        url = "http://127.0.0.1:8000/api/v1/courses/"
        response = self.client.post(url, data={
                "title": "example_title",
                "description": "example_description",
                "sub_title": "example_sub_title",
                "language": "en",
                "level": "example",
                "price": "99.99",
                "category": "Development",
                "sub_category": "Web Development",
                "secondery_category": "Python",
                "image": "example"
            },
            **self.bearer_token
        )
        
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED,
            print(response.data)
        )