from django.db import models

# Create your models here.

class Product(models.Model):
    genre = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

