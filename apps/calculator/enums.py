import copy
from enum import Enum, EnumMeta
from typing import Any

from django.db.models.enums import ChoicesMeta


class CustomEnumMeta(EnumMeta):

    @property
    def choices(cls):
        return [(instance.name, instance.value[0]) for instance in cls]

    def to_dict(cls):
        result: dict = {}
        for instance in cls:
            instance_info: dict = copy.deepcopy(instance.__dict__)
            del instance_info['__objclass__']
            result[instance.name] = instance_info
        return result


class CustomEnum(Enum, metaclass=CustomEnumMeta):
    pass


class ChargeType(CustomEnum):
    WEIGHT = ('무게', 'kg')
    VOLUME = ('부피', 'm<sup>3</sup>')

    def __init__(self, kr_name, unit_html):
        self.kr_name = kr_name
        self.unit_html = unit_html


class LorryType(CustomEnum):
    SMALL = ('작은차', 1740, 1970, 1000, 300)
    MEDIUM = ('중간차', 2460, 2670, 5000, 500)
    LARGE = ('큰차', 3000, 3000, 10000, 700)

    def __init__(self, kr_name, width, height, loadable_weight, loadable_volume):
        self.kr_name = kr_name
        self.width = width
        self.height = height
        self.loadable_weight = loadable_weight
        self.loadable_volume = loadable_volume
