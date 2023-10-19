from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer
from .serializers import CustomerSerializer, CustomerFullSerializer


class CustomerGetView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            security_code = serializer.validated_data['security_code']

            queryset = Customer.objects.filter(phone_number=phone_number, security_code=security_code)
            obj = queryset.first()
            if obj is not None:
                serialized_obj = CustomerFullSerializer(obj)
                return Response(serialized_obj.data, status=status.HTTP_200_OK)
            return Response({'status': 'User topilmadi!'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
