from django.contrib import admin
from application.feedback.models import (
    Comment, Rating, LikeComment
)

admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(LikeComment)