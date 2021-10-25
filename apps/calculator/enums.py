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
    ONE_TONE = ('1톤', 1500, 2800, 800, 1000)
    ONE_HALF_TONE = ('1.4톤', 1550, 3100, 800, 1500)
    TWO_HALF_TONE = ('2.5톤', 1900, 4300, 1030, 25000)
    THREE_HALF_TONE = ('3.5톤', 2090, 4500, 1050, 3500)
    FIVE_TONE = ('4.5톤-5톤', 2280, 6250, 1100, 5000)
    FIVE_TONE_PLUS = ('5톤 플러스', 2300, 7250, 1200, 5000)
    SIX_HALF_TONE = ('6.5톤 플러스축', 2350, 7400, 1200, 6500)
    ELEVEN_TONE = ('11톤', 2350, 9100, 1400, 11000)
    FOURTEEN_TONE = ('14톤', 2350, 9300, 1400, 14000)
    EIGHTEEN_TONE = ('18톤', 2350, 10100, 1400, 18000)
    TWENTY_FIVE_TONE = ('25톤', 2350, 10100, 1400, 25000)
    TRAILER = ('트레일러', 2500, 12000, 1600, 30000)
    LOW_BED_TRAILER = ('로베드', 2500, 5600, 800, 30000)

    def __init__(self, kr_name, width,length, height, loadable_weight):
        self.kr_name = kr_name
        self.width = width
        self.length = length
        self.height = height
        self.loadable_weight = loadable_weight

