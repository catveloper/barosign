from django.forms import ModelForm

from apps.calculator.models import Freight


class CalculatorForm(ModelForm):
    class Meta:
        model = Freight
        fields = "__all__"
