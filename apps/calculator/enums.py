from enum import Enum

from django.db.models.enums import ChoicesMeta


class CustomChoiceMeta(ChoicesMeta):

    @property
    def choices(cls):
        return [(instance.name, instance.value[0]) for instance in cls]


class Choices(Enum, metaclass=CustomChoiceMeta):
    pass


class PriceType(Choices):
    WEIGHT = ('무게',)
    VOLUME = ('부피',)

    def __init__(self, kr_name):
        self.kr_name = kr_name
