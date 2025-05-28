from PIL import Image
from django.db import models
from .util.helpers import resize_image 

class Teammate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team", null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    youtube = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="category", null=True, blank=True)
    #resize image to width 500px and height 300px
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Resize the image to width 500px and height 300px
        resize_image(self.image, size=(500, 300))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]

class Stall(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="stall", null=True, blank=True, help_text="Upload an image for the stall. Recommended size: 500x300 pixels. This field can be left blank if no image is available.")
    cohort_name = models.CharField(max_length=100, null=True, blank=True)
    cohort_year = models.CharField(max_length=4, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    specifics = models.TextField(null=True, blank=True)
    links = models.TextField(null=True, blank=True)
    other_details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name="stalls", help_text="Select categories for the stall. You can choose multiple categories or just one.")
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Resize the image to width 500px and height 300px
        resize_image(self.image, size=(500, 300))

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="product", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stall = models.ForeignKey(Stall, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Resize the image to width 500px and height 300px
        resize_image(self.image, size=(500, 300))

