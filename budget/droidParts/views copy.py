from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DroidParts
from .serializers import DroidPartsSerializer

class DroidPartsAPIView(APIView):
  """ 
  API Budget Droid Parts
  """
  def get(self, request):
    droidParts = DroidParts.objects.all()
    serializer = DroidPartsSerializer(droidParts, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = DroidPartsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)