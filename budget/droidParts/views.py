from rest_framework import generics

from .models import DroidParts
from .serializers import DroidPartsSerializer

class DroidsPartsAPIView(generics.ListCreateAPIView):
  queryset = DroidParts.objects.all()
  serializer_class = DroidPartsSerializer
  
  
class DroidPartsAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = DroidParts.objects.all()
  serializer_class = DroidPartsSerializer
  