from rest_framework import viewsets, permissions, status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import ChargeCalculatorSerializer, TransportSectionSerializer
from apps.calculator.enums import TruckType
from apps.calculator.models import ChargeCalculator, ChargeType, TransportSection


class ChargeCalculatorViewSet(ModelViewSet):
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
        real_distance = float(data['distance']) + charge_type.section.extra_distance
        cost = charge_type.per_km_cost * real_distance
        if load_ratio <= 40:
            cost = cost * truck.less_load_discount
        data['distance'] = real_distance
        data['cost'] = int(cost)
        data['charge_type'] = charge_type.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data['cost'], status=status.HTTP_201_CREATED, headers=headers)


class TransportSectionViewSet(UpdateAPIView):
    queryset = TransportSection.objects.all()
    serializer_class = TransportSectionSerializer
    permission_classes = [permissions.AllowAny]

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)