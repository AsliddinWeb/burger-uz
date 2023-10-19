from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import action

from .models import Customer
from .serializers import CustomerSerializer, CustomerFullSerializer

class CreateCustomer(APIView):
    def post(self, request, format=None):
        serializer = CustomerFullSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetCustomerByPhone(APIView):
    def post(self, request, format=None):
        phone_number = request.data.get('phone_number')
        security_code = request.data.get('security_code')

        try:
            customer = Customer.objects.get(phone_number=phone_number, security_code=security_code)
            serializer = CustomerFullSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"error": "Mijoz topilmadi."}, status=status.HTTP_404_NOT_FOUND)