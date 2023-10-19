from django.db import models

from customer_app.models import Customer
from driver_app.models import Driver
from payment_app.models import Payment

class OrderStatus(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(Payment, on_delete=models.CASCADE)

    delivery_address = models.TextField()
    order_items = models.TextField()
    total_price = models.BigIntegerField(null=True, blank=True)

    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
