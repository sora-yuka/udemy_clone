from django.db import models
from application.course.models import Course
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses")
    
    def __str__(self):
        return self.course
    

class Archive(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="archives")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="archives")

    def __str__(self):
        return self.owner