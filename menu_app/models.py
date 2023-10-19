from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product-categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='menu')
    description = models.TextField()
    price = models.BigIntegerField()
    preparation_time = models.BigIntegerField()

    def __str__(self):
        return self.title