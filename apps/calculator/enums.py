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


class TruckType(CustomEnum):
    ONE_TONE = ('1톤', 150, 280, 100, 1000, 1000, 0.9)
    ONE_HALF_TONE = ('1.4톤', 155, 310, 100, 1500, 1500, 0.9)
    TWO_HALF_TONE = ('2.5톤', 190, 430, 103, 25000, 25000, 0.9)
    THREE_HALF_TONE = ('3.5톤', 209, 450, 105, 3500, 3500, 0.9)
    FIVE_TONE = ('5톤', 228, 625, 110, 5000, 5000, 0.9)
    FIVE_TONE_PLUS = ('5톤 플러스', 230, 725, 120, 5000, 5000, 0.9)
    SIX_HALF_TONE = ('6.5톤', 235, 740, 120, 6500, 6500, 0.95)
    ELEVEN_TONE = ('11톤', 235, 910, 140, 11000, 11000, 0.95)
    FOURTEEN_TONE = ('14톤', 235, 930, 140, 14000, 14000, 0.95)
    EIGHTEEN_TONE = ('18톤', 235, 1010, 140, 18000, 18000, 0.95)
    TWENTY_FIVE_TONE = ('25톤', 235, 1010, 140, 25000, 25000, 0.95)
    TRAILER = ('트레일러', 250, 1200, 160, 30000, 30000, 0.95)
    LOW_BED_TRAILER = ('로베드', 250, 560, 100, 30000, 30000, 0.95)

    def __init__(self, kr_name, width, length, height, weight, loadable_weight, less_load_discount):
        self.kr_name = kr_name
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.loadable_weight = loadable_weight
        self.less_load_discount = less_load_discount
