from rest_framework import generics

from .models import OrderProduct
from .serializers import OrderProductSerializer


class OrderProductList(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = OrderProduct.objects.filter(created_by=self.request.user.id)
        return queryset

    serializer_class = OrderProductSerializer


class OrderProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
