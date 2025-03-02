from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Image(models.Model):
    id = models.AutoField(primary_key = True)
    file = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    uploaded_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return  f'Image {self.id} : {self.description[:30]}'






# Create your models here.
