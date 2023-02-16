from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

LANGUAGE = (
    ("Русский", "Русский"),
    ("Английский", "Английский")
)

LEVEL = (
    ("Начальный", "Начальный"),
    ("Продвинутый", "Продвинутый"),
    ("Профессиональный", "Профессиональный"),
)


class Category(models.Model):
    category = models.SlugField(primary_key=True)
    
#?  По желанию можно добавить.
    """
    sub_category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, 
        blank=True, null=True, related_name="sub_categorys"
    )
    """    
    def __str__(self):
        return self.category
    

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=55)
    sub_title = models.CharField(max_length=155)
    language = models.CharField(max_length=25, choices=LANGUAGE)
    level = models.CharField(max_length=25, choices=LEVEL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # image = models.ImageField(upload_to="image/") -->  не забыть довабить поле картинок.
    # video = models.FieldFile()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title


class ProductItem(models.Model):
    course = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=185)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    
class ProductFile(models.Model):
    course_item_id = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name="files")
    course_file = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"{self.course_file}"


class Archive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="archives")
    course = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="archives")
    
    def __str__(self):
        return f"{self.user} - archived course - {self.course}"