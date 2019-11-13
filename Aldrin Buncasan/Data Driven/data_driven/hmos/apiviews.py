from rest_framework import generics

from .models import Hmo
from .serializers import HmoSerializer

class HmoList(generics.ListCreateAPIView):
    queryset = Hmo.objects.all()
    serializer_class = HmoSerializer


class HmoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hmo.objects.all()
    serializer_class = HmoSerializer