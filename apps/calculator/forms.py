from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet
from extra_views import InlineFormSetFactory

from apps.calculator.enums import TruckType
from apps.calculator.models import TransportSection, ChargeCalculator, ChargeType

# TODO: unique field 에대한 validation
class TransportSectionForm(forms.ModelForm):

    class Meta:
        model = TransportSection
        fields = [
            "start_area",
            "arrival_area",
            "extra_distance",
        ]
        initial = {
            "extra_distance": 0
        }


class ChargeTypeForm(forms.ModelForm):

    truck = forms.ChoiceField(
        label='',
        choices=TruckType.choices,
        disabled=True
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
    prefix = 'chargeType'
    initial = [{'truck': truck.name} for truck in TruckType]
    factory_kwargs = {'min_num': len(TruckType), 'max_num': len(TruckType), 'can_delete_extra': False}


ChargeTypeFormSet = inlineformset_factory(TransportSection, ChargeType, form=ChargeTypeForm, extra=len(TruckType), max_num=len(TruckType), can_delete_extra=False)


class ChargeCalculatorForm(forms.ModelForm):
    transport_section = forms.ModelChoiceField(
        label=TransportSection._meta.verbose_name,
        queryset=TransportSection.objects.filter(is_use=True),
        empty_label="구간을 선택해주세요"
    )
    truck = forms.ChoiceField(
        label='화물차',
        choices=TruckType.choices,
    )
    distance = forms.IntegerField(
        label=ChargeCalculator.distance.field.verbose_name,
        help_text='T_MAP API 연동을 통해서 자동 계산되는 항목입니다',
        widget=forms.NumberInput({
            'readonly': True
        })
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
