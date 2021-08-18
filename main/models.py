from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumbers import phonenumber

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phonenumber = PhoneNumberField()
    address = models.CharField(max_length=80)


# Person.objects.create(name = 'yossi', email = 'hutf@dg', phonenumber= '+12125552368', address = 'yuy12')