from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone =  PhoneField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} Profile'






