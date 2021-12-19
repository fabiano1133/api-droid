from django.db import models

class DroidParts(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField(max_length=255)
  delivery_address = models.CharField(max_length=255)
  email_contact = models.EmailField(max_length=255)
  advertiser = models.CharField(max_length=255)
  isDone = models.BooleanField(default=False)
  
  class Meta:
    verbose_name = 'Droid Part'
    verbose_name_plural = 'Droid Parts'
    
  def __str__(self):
    return self.title