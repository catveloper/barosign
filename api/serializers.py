from rest_framework import serializers

from apps.calculator.models import ChargeCalculator


class ChargeCalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeCalculator
        fields = [
            "charge_type",
            "freight_name",
            "load_weight",
            "start_point",
            "arrival_point",
            "distance",
            "cost",
        ]

