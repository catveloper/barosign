from django.db import models

from apps.calculator.enums import TruckType


class ChargeTypeQuerySet(models.QuerySet):

    def get_charge_type_by_truck(self, section_id, truck):
        if type(truck) == TruckType:
            truck = truck.name
        return self.filter(section_id=section_id, truck=truck).first()
