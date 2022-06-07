from django.db import models
from django.contrib.auth.models import User


class Customers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField(max_length=11)
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    cpf = models.IntegerField(max_length=11, unique=True)
    
    def __str__(self):
        return self.name
