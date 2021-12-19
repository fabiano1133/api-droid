from django.contrib import admin

from .models import DroidParts


@admin.register(DroidParts)
class DroidPartsAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'delivery_address', 'email_contact', 'advertiser', 'isDone')
  
