from django.db import models
from django.contrib.auth import get_user_model
from application.course.choices import *

User = get_user_model()


class Category(models.Model):
    category = models.CharField(max_length=60, primary_key=True, default="Development")
    
    def __str__(self):
        return self.category
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name="sub_categorys",
    )
    sub_category = models.CharField(max_length=60, primary_key=True, default="Web Development")
    
    def __str__(self):
        return self.sub_category
    
    
class SeconderyCategory(models.Model):
    sub_category = models.ForeignKey(
        SubCategory, on_delete = models.CASCADE, 
        related_name="secondery_categorys",
    )
    secondery_category = models.CharField(max_length=60, primary_key=True, default="Python")
    
    def __str__(self):
        return self.secondery_category
    

class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="course_owner")
    title = models.CharField(max_length=60)
    sub_title = models.CharField(max_length=60)
    language = models.CharField(max_length=25, choices=LANGUAGE)
    level = models.CharField(max_length=25, choices=LEVEL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course_category")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="course_subcategory")
    secondery_category = models.ForeignKey(SeconderyCategory, on_delete=models.CASCADE, related_name="course_secondery_category")
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # image = models.ImageField(upload_to="image/") -->  не забыть довабить поле картинок.
    # video = models.FieldFile()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title


class CourseItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=185)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    
class CourseFile(models.Model):
    course_item_id = models.ForeignKey(CourseItem, on_delete=models.CASCADE, related_name="files")
    course_file = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"{self.course_file}"
