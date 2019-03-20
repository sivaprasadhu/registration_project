from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=45)
    password1 = models.CharField(max_length=25)
    password2 = models.CharField(max_length=25)
