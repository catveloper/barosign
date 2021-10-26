from django.urls import path

from apps.calculator.views import *

app_name = 'calculator'

urlpatterns = [
    path('', CalculatorFV.as_view(), name='index'),
    path('transport-section/add', TransportSectionCV.as_view(), name='transport_section_cv'),
    path('transport-section/<int:pk>', TransportSectionUV.as_view(), name='transport_section_uv'),
    path('transport-section/', TransportSectionLV.as_view(), name='transport_section_lv'),
]
