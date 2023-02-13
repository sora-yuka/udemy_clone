from django.db import models
from application.products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    course = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="courses")
    
    def __str__(self):
        return self.course