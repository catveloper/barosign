from django.urls import path, include, reverse
from rest_framework.routers import DefaultRouter

from api.viewsets import *

app_name = 'api'


router = DefaultRouter()
router.register(r'calculators', viewset=ChargeCalculatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('transport-sections/<int:pk>/', TransportSectionViewSet.as_view(), name='transport_section_update'),
]

