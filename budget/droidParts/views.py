# from rest_framework import generics
from rest_framework import viewsets


from .models import DroidParts
from .serializers import DroidPartsSerializer


"""
API V1
"""

# class DroidsPartsAPIView(generics.ListCreateAPIView):
#   queryset = DroidParts.objects.all()
#   serializer_class = DroidPartsSerializer
  
  
# class DroidPartsAPIView(generics.RetrieveUpdateDestroyAPIView):
#   queryset = DroidParts.objects.all()
#   serializer_class = DroidPartsSerializer
 
"""
API V2
"""

class DroidsPartsViewSet(viewsets.ModelViewSet):
  queryset = DroidParts.objects.all()
  serializer_class = DroidPartsSerializer