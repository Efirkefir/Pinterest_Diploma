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
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'images', verbose_name="Категория")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images', verbose_name="Пользователь")
    uploaded_at = models.DateTimeField(auto_now_add = True, verbose_name="Дата загрузки")
    updated_at = models.DateTimeField(auto_now = True, verbose_name="Дата обновления")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата удаления")

    def __str__(self):
        return  f'Image {self.id} : {self.description[:30]}'







