from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class DriverType(models.Model):
    title = models.CharField(max_length=255)
    price = models.BigIntegerField(default=0)
    speed = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    driver_type = models.ForeignKey(DriverType, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
