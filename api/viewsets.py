from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from api.serializers import ChargeCalculatorSerializer
from apps.calculator.enums import TruckType
from apps.calculator.models import ChargeCalculator, ChargeType


class ChargeCalculatorViewSet(viewsets.ModelViewSet):
    queryset = ChargeCalculator.objects.all()
    serializer_class = ChargeCalculatorSerializer
    permission_classes = [permissions.AllowAny]


    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        truck = TruckType[data['truck']]
        charge_type: ChargeType = ChargeType.objects.get_charge_type_by_truck(data['transport_section'], truck)
        load_weight = data['load_weight']
        loadable_weight = truck.loadable_weight
        load_ratio = (float(load_weight)/loadable_weight) * 100
        cost = charge_type.per_km_cost * float(data['distance'])
        if load_ratio <= 40:
            cost = cost * truck.less_load_discount
        data['cost'] = int(cost)
        data['charge_type'] = charge_type.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data['cost'], status=status.HTTP_201_CREATED, headers=headers)
