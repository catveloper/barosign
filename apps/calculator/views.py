from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from apps.calculator.forms import CalculatorForm


class CalculatorFV(FormView):
    template_name = 'calculator/form.html'
    form_class = CalculatorForm
