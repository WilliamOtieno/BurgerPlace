from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)

class SubOrder(models.Model):
    quantity = models.CharField(max_length=200)
