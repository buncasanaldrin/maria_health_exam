from rest_framework import generics

from .models import PaymentTerm
from .serializers import PaymentTermSerializer


class PaymentTermList(generics.ListCreateAPIView):
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializer


class PaymentTermDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializer
