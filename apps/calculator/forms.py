from django import forms
from django.forms import inlineformset_factory

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
            "start_ara",
            "arrival_are",
            "extra_distance",
        ]


class ChargeTypeForm(forms.ModelForm):

    class Meta:
        model = ChargeType
        fields = [
            "truck",
            "per_km_cost",
        ]


ChargeTypeFormSet = inlineformset_factory(parent_model=TransportSection, model=ChargeType, form=ChargeTypeForm, extra=len(TruckType), can_delete_extra=False)


class ChargeCalculatorForm(forms.ModelForm):
    freight = forms.ModelChoiceField(
        label=ChargeCalculator.chargeType.field.verbose_name,
        queryset=TransportSection.objects.filter(is_use=True),
        to_field_name='name'
    )
    load_weight = forms.IntegerField(
        label=ChargeCalculator.load_weight.field.verbose_name,
        widget=forms.TextInput()
    )
    distance = forms.IntegerField(
        label=ChargeCalculator.distance.field.verbose_name,
        widget=forms.TextInput({'disabled':True}),
        help_text='T_MAP API 연동을 통해서 자동 계산되는 항목입니다'
    )
    # class Meta:
    #     model = ChargeCalculator
    #     fields = [
    #         "freight",
    #         "load_weight",
    #         "load_volume",
    #         "start_point",
    #         "arrival_point",
    #         "distance",
    #     ]
