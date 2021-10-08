from enum import Enum, EnumMeta

from django.db.models.enums import ChoicesMeta


class CustomChoiceMeta(EnumMeta):

    @property
    def choices(cls):
        return [(instance.name, instance.value[0]) for instance in cls]


class CustomChoices(Enum, metaclass=CustomChoiceMeta):
    pass


class ChargeType(CustomChoices):
    WEIGHT = ('무게', 'kg')
    VOLUME = ('부피', 'm^3')

    def __init__(self, kr_name, unit):
        self.kr_name = kr_name
        self.unit = unit

