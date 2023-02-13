from django.db import models
from application.products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

RATE = (
    ("☆☆☆☆☆", "☆☆☆☆☆"),
    ("☆☆☆☆", "☆☆☆☆"),
    ("☆☆☆", "☆☆☆"),
    ("☆☆", "☆☆"),
    ("☆", "☆")
)
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    courses = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    rate = models.CharField(max_length=15, choices=RATE)
    
    def __str__(self):
        return f"{self.courses} {self.rate}"
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    courses = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.comment[:7]}..."
    
    
class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_comment")
    courses = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="likes_comment")
    course_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="like_comment")
    like = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Liked - {self.courses}"
