# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from apps.calculator.enums import ChargeType
from apps.calculator.forms import FreightForm
from apps.calculator.models import Freight


class CalculatorFV(FormView):
    template_name = 'calculator/index.html'
    success_url = reverse_lazy('calculator:freight_lv')
    form_class = FreightForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['chargeType'] = ChargeType.to_dict()
        return context_data

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FreightLV(ListView):
    template_name = 'calculator/freight/list.html'
    model = Freight
    paginate_by = 10
    ordering = 'create_dt'


class FreightFV(FormView):
    template_name = 'calculator/freight/form.html'
    success_url = reverse_lazy('calculator:freight_lv')
    form_class = FreightForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['chargeType'] = ChargeType.to_dict()
        return context_data

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
