from rest_framework.viewsets import ModelViewSet

# Auth
from rest_framework.permissions import IsAuthenticated

from .serializers import PaymentSerializer
from .models import Payment

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    