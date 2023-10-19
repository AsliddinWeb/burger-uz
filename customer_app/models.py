from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    tg_id = models.BigIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    delivery_address = models.TextField(null=True, blank=True)
    is_ordered = models.BooleanField(default=False)
    security_code = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name