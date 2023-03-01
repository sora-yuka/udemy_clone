from django.db import models
from django.contrib.auth import get_user_model
from application.course.models import Course


User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="favorites")
    
    def __str__(self):
        return self.course