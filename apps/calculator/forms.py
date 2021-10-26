from django import forms
from django.forms import inlineformset_factory
from extra_views import InlineFormSetFactory

from apps.calculator.enums import TruckType
from apps.calculator.models import TransportSection, ChargeCalculator, ChargeType


class TransportSectionForm(forms.ModelForm):
    extra_distance = forms.IntegerField(
        label=TransportSection.extra_distance.field.verbose_name,
        widget=forms.TextInput()
    )

    class Meta:
        model = TransportSection
        fields = [
            "start_area",
            "arrival_area",
            "extra_distance",
        ]


class ChargeTypeForm(forms.ModelForm):
    truck = forms.ChoiceField(
        label='',
        choices=TruckType.choices
    )
    per_km_cost = forms.IntegerField(
        label='',
    )

    class Meta:
        model = ChargeType
        fields = [
            "truck",
            "per_km_cost",
        ]


class ChargeTypeInline(InlineFormSetFactory):
    model = ChargeType
    form_class = ChargeTypeForm
    initial = [{'truck': truck.name} for truck in TruckType]
    prefix = 'charge-type-form'
    factory_kwargs = {'extra': len(TruckType), 'can_delete_extra': False}


class ChargeCalculatorForm(forms.ModelForm):
    transport_section = forms.ModelChoiceField(
        label=TransportSection._meta.verbose_name,
        queryset=TransportSection.objects.filter(is_use=True),
        to_field_name='name'
    )
    truck = forms.ChoiceField(
        label='화물차',
        choices=TruckType.choices,
    )
    load_weight = forms.IntegerField(
        label=ChargeCalculator.load_weight.field.verbose_name,
        widget=forms.TextInput()
    )
    distance = forms.IntegerField(
        label=ChargeCalculator.distance.field.verbose_name,
        widget=forms.TextInput({'disabled': True}),
        help_text='T_MAP API 연동을 통해서 자동 계산되는 항목입니다'
    )

    class Meta:
        model = ChargeCalculator
        fields = [
            'freight_name',
            'load_weight',
            'start_point',
            'arrival_point',
            'distance',
        ]
