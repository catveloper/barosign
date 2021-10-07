from django import forms

from apps.calculator.enums import ChargeType
from apps.calculator.models import Freight


class FreightForm(forms.ModelForm):
    charge_per_weight = forms.IntegerField(
        label='무게당 금액',
        widget=forms.NumberInput({'placeholder': '무게 1kg당 금액을 입력해주세요'})
    )
    charge_per_volume = forms.IntegerField(
        label='부피당 금액',
        widget=forms.NumberInput({'placeholder': '부피 1m3당 금액을 입력해주세요'})
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
