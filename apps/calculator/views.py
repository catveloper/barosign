# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from extra_views import CreateWithInlinesView, NamedFormsetsMixin, UpdateWithInlinesView

from apps.calculator.enums import TruckType
from apps.calculator.forms import TransportSectionForm, ChargeCalculatorForm, ChargeTypeInline
from apps.calculator.models import TransportSection, ChargeType


class CalculatorFV(CreateView):
    template_name = 'calculator/index.html'
    success_url = reverse_lazy('calculator:index')
    form_class = ChargeCalculatorForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['truck_type'] = TruckType.to_dict()
        return context_data

    def form_invalid(self, form):
        form['charge_type'] = ChargeType.objects.filter(transport_section_id=form.transport_section,
                                                        truck=form.truck).first().id
        return super().form_invalid(form)


class TransportSectionLV(ListView):
    template_name = 'calculator/transport_section/list.html'
    model = TransportSection
    paginate_by = 10
    ordering = 'create_dt'


class TransportSectionCV(NamedFormsetsMixin, CreateWithInlinesView):
    model = TransportSection
    template_name = 'calculator/transport_section/form.html'
    success_url = reverse_lazy('calculator:transport_section_lv')
    form_class = TransportSectionForm
    inlines = [ChargeTypeInline]
    inlines_names = ['charge_types']

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['truck_type'] = TruckType.to_dict()
        return context_data


class TransportSectionUV(NamedFormsetsMixin, UpdateWithInlinesView):
    model = TransportSection
    template_name = 'calculator/transport_section/form.html'
    success_url = reverse_lazy('calculator:transport_section_lv')
    form_class = TransportSectionForm
    inlines = [ChargeTypeInline]
    inlines_names = ['charge_types']

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['truck_type'] = TruckType.to_dict()
        return context_data

