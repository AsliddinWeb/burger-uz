from django.urls import path

from .views import CustomerGetView


urlpatterns = [
    path('', CustomerGetView.as_view(), name='customer-detail'),
]
