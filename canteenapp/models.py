from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=30,default="User")
    email=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)


class orders(models.Model):
    name = models.CharField(max_length=30)
    mobileno = models.CharField(max_length=12)
    fooditem = models.CharField(max_length=20)
    quantity = models.CharField(max_length=10)
    price = models.IntegerField()
