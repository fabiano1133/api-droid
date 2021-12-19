from rest_framework import serializers

from .models import DroidParts

class DroidPartsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = DroidParts
    fields = (
      'id',
      'title',
      'description',
      'delivery_address',
      'email_contact',
      'advertiser',
      'isDone'
    )