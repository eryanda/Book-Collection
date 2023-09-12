from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default="Title")
    amount = models.IntegerField()
    description = models.TextField()

