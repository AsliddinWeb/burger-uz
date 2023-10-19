from rest_framework import routers
from django.urls import path, include

from .views import PaymentViewSet

routers = routers.DefaultRouter()
routers.register(r'', PaymentViewSet)

urlpatterns = [
    path('', include(routers.urls))
]