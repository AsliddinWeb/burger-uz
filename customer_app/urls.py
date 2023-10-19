from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CreateCustomer, GetCustomerByPhone


urlpatterns = [
    path('create/', CreateCustomer.as_view()),
    path('get/', GetCustomerByPhone.as_view())
]

