from django.urls import path

from apps.calculator.views import *

app_name = 'calculator'

urlpatterns = [
    path('', CalculatorFV.as_view(), name='index'),
    path('freights/add', FreightCV.as_view(), name='freight_cv'),
    path('freights/<int:pk>', FreightUV.as_view(), name='freight_uv'),
    path('freights/', FreightLV.as_view(), name='freight_lv'),
]
