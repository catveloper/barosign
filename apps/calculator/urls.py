from django.urls import path

from apps.calculator.views import FreightFV

app_name = 'calculator'

urlpatterns = [
    path('freight/', FreightFV.as_view(), name='freight'),
]
