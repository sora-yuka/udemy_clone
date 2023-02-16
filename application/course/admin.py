from django.contrib import admin
from application.course.models import (
    Course, CourseFile, CourseItem, Category
)

admin.site.register(Course)
admin.site.register(CourseFile)
admin.site.register(CourseItem)
admin.site.register(Category)