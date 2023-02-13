from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    competence = models.CharField(max_length=85, blank=True)
    language = models.CharField(max_length=55, blank=True)
    site_url = models.CharField(max_length=85, blank=True)
    twitter_url = models.CharField(max_length=85, blank=True)
    facebook_url = models.CharField(max_length=85, blank=True)
    linkedin_url = models.CharField(max_length=85, blank=True)
    youtube_url = models.CharField(max_length=85, blank=True)
    is_hidden = models.BooleanField(default=False)
    is_hidden_courses = models.BooleanField(default=False)
    promotions = models.BooleanField(default=False)
    mentor_ads = models.BooleanField(default=False)
    email_ads = models.BooleanField(default=False)
    image = models.ImageField(upload_to="image/")