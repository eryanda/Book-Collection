from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

