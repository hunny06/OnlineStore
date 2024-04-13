from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length = 100)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    stock = models.IntegerField()
    discription = models.TextField()
    sold = models.BooleanField()
    prize = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name