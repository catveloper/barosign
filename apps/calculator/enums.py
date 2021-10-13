from enum import Enum, EnumMeta

from django.db.models.enums import ChoicesMeta


class CustomEnumMeta(EnumMeta):

    @property
    def choices(cls):
        return [(instance.name, instance.value[0]) for instance in cls]


class CustomEnum(Enum, metaclass=CustomEnumMeta):

    @classmethod
    def to_dict(cls):
        return {instance.name: instance for instance in cls}


class ChargeType(CustomEnum):
    WEIGHT = ('무게', 'kg')
    VOLUME = ('부피', 'm<sup>3</sup>')

    def __init__(self, kr_name, unit_html):
        self.kr_name = kr_name
        self.unit_html = unit_html


