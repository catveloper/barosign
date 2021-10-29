from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.viewsets import ChargeCalculatorViewSet

app_name = 'api'


router = DefaultRouter()
router.register(r'calculators', viewset=ChargeCalculatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]