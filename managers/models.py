from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Manager(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}. {self.user.username}'

