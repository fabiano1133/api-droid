from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
  # DroidsPartsAPIView, 
  # DroidPartsAPIView,
  DroidsPartsViewSet
)

router = SimpleRouter()
router.register('budgets', DroidsPartsViewSet)

# urlpatterns = [
#   path('budgets/', DroidsPartsAPIView.as_view(), name='budgets'),
#   path('budgets/<int:pk>/', DroidPartsAPIView.as_view(), name='budget')
# ]