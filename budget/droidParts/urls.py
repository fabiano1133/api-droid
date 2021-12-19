from django.urls import path

from .views import DroidPartsAPIView

urlpatterns = [
  path('budgets/', DroidPartsAPIView.as_view(), name='budgets'),
]