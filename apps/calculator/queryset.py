from django.db import models

from apps.calculator.enums import TruckType


class TransportSectionQuerySet(models.QuerySet):

    def get_charge_type_by_truck(self, pk, truck):
        if type(truck) == TruckType:
            truck = truck.name
        return self.filter(pk=pk, charge_types__truck=truck)