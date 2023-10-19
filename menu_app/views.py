from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework.viewsets import ModelViewSet

# Auth
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
