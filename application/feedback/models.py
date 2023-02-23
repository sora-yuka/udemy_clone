from django.db import models
from application.course.models import Course
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="ratings")
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(10),
        ], 
        blank=True, null=True
    )
    
    def __str__(self):
        return f"{self.courses} {self.rating}"
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} - {self.comment[:7]}..."
    
    
class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_comment")
    course_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes_comment")
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Liked - {self.course_comment}"
