from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView

from apps.calculator.forms import FreightForm
from apps.calculator.models import Freight


class FreightFV(FormView):
    template_name = 'calculator/freight/form.html'
    success_url = reverse_lazy('calculator:freight_lv')
    form_class = FreightForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FreightLV(ListView):
    template_name = 'calculator/freight/list.html'
    model = Freight
