from django.urls import path

from apps.calculator.views import *

app_name = 'calculator'

urlpatterns = [
    path('freight/', FreightFV.as_view(), name='freight_fv'),
    path('freights/', FreightLV.as_view(), name='freight_lv'),
]