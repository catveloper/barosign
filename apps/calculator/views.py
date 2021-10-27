# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from extra_views import CreateWithInlinesView, NamedFormsetsMixin

from apps.calculator.enums import TruckType
from apps.calculator.forms import TransportSectionForm, ChargeCalculatorForm, ChargeTypeInline, ChargeTypeFormSet
from apps.calculator.models import TransportSection, ChargeType


class CalculatorFV(CreateView):
    template_name = 'calculator/index.html'
    success_url = reverse_lazy('calculator:index')
    form_class = ChargeCalculatorForm

    def get_context_dataㄴ(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['truckType'] = TruckType.to_dict()
        return context_data

    def form_invalid(self, form):
        form['chargeType'] = ChargeType.objects.filter(transport_section_id=form.transport_section,
                                                       truck=form.truck).first().id
        return super().form_invalid(form)


class TransportSectionLV(ListView):
    template_name = 'calculator/transport_section/list.html'
    model = TransportSection
    paginate_by = 10
    ordering = 'create_dt'


class TransportSectionCV(NamedFormsetsMixin, CreateWithInlinesView):
    template_name = 'calculator/transport_section/form.html'
    success_url = reverse_lazy('calculator:transport_section_lv')
    form_class = TransportSectionForm
    model = TransportSection
    inlines = [ChargeTypeInline]
    inlines_names = ['charge_types']

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    #
    # def forms_valid(self, form, inlines):
    #     return super(TransportSectionCV, self).forms_valid()
    #
    # def forms_invalid(self, form, inlines):
    #     context_data = self.get_context_data(form=form, inlines=inlines)
    #     context_data['charge_types'] = ChargeTypeInline(self.model, self.request, self.object).get_formset()
    #     response = self.render_to_response(context_data)
    #     return response


# class TransportSectionCV(CreateView):
#     template_name = 'calculator/transport_section/form.html'
#     success_url = reverse_lazy('calculator:transport_section_lv')
#     form_class = TransportSectionForm
#     formset_class = ChargeTypeFormSet
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context_data['charge_type_forms'] = ChargeTypeFormSet(self.request.POST)
#         else:
#             context_data['charge_type_forms'] = ChargeTypeFormSet(initial=[{'truck': truck.name} for truck in TruckType])
#         return context_data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         charge_type_forms = context['charge_type_forms']
#         if charge_type_forms.is_valid():
#             self.object = form.save()
#             charge_type_forms.instance = self.object
#             charge_type_forms.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))


class TransportSectionUV(UpdateView):
    model = TransportSection
    template_name = 'calculator/transport_section/form.html'
    success_url = reverse_lazy('calculator:transport_section_lv')
    form_class = TransportSectionForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['truckType'] = TruckType.to_dict()
        return context_data
