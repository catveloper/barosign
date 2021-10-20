from django import forms

from apps.calculator.models import Freight, ChargeCalculator


class FreightForm(forms.ModelForm):
    rate_conversion_point = forms.IntegerField(
        label='요금기준 전환점',
        widget=forms.TextInput()
    )
    charge_per_weight = forms.IntegerField(
        label='무게당 금액',
        widget=forms.TextInput({'placeholder': '무게 1kg당 금액을 입력해주세요'})
    )
    charge_per_volume = forms.IntegerField(
        label='부피당 금액',
        widget=forms.TextInput({'placeholder': '부피 1m3당 금액을 입력해주세요'})
    )

    class Meta:
        model = Freight
        fields = [
            "name",
            "priority",
            "rate_conversion_point",
            "charge_per_weight",
            "charge_per_volume",
        ]


class ChargeCalculatorForm(forms.ModelForm):
    freight = forms.ModelChoiceField(
        label=ChargeCalculator.freight.field.verbose_name,
        queryset=Freight.objects.filter(is_use=True),
        to_field_name='name'
    )
    load_weight = forms.IntegerField(
        label=ChargeCalculator.load_volume.field.verbose_name,
        widget=forms.TextInput()
    )
    load_volume = forms.IntegerField(
        label=ChargeCalculator.load_volume.field.verbose_name,
        widget=forms.TextInput()
    )
    distance = forms.IntegerField(
        label=ChargeCalculator.distance.field.verbose_name,
        widget=forms.TextInput({'disabled':True}),
        help_text='T_MAP API 연동을 통해서 자동 계산되는 항목입니다'
    )
    class Meta:
        model = ChargeCalculator
        fields = [
            "freight",
            "load_weight",
            "load_volume",
            "start_point",
            "arrival_point",
            "distance",
        ]
