from django.urls import path

from .views import DroidsPartsAPIView, DroidPartsAPIView

urlpatterns = [
  path('budgets/', DroidsPartsAPIView.as_view(), name='budgets'),
  path('budgets/<int:pk>/', DroidPartsAPIView.as_view(), name='budget')
]