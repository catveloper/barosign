# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView

from apps.calculator.enums import TruckType
from apps.calculator.forms import TransportSectionForm, ChargeCalculatorForm
from apps.calculator.models import TransportSection


class CalculatorFV(CreateView):
    template_name = 'calculator/index.html'
    success_url = reverse_lazy('calculator:index')
    form_class = ChargeCalculatorForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['chargeType'] = TruckType.to_dict()
        return context_data


class FreightLV(ListView):
    template_name = 'calculator/freight/list.html'
    model = TransportSection
    paginate_by = 10
    ordering = 'create_dt'


class FreightCV(CreateView):
    template_name = 'calculator/freight/form.html'
    success_url = reverse_lazy('calculator:freight_lv')
    form_class = TransportSectionForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['chargeType'] = TruckType.to_dict()
        return context_data


class FreightUV(UpdateView):
    model = TransportSection
    template_name = 'calculator/freight/form.html'
    success_url = reverse_lazy('calculator:freight_lv')
    form_class = TransportSectionForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['chargeType'] = TruckType.to_dict()
        return context_data
