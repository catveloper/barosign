# Create your models here.
from django.db import models

from apps.calculator.enums import TruckType


class TransportSection(models.Model):

    start_ara = models.CharField('출발 지역', max_length=100)
    arrival_are = models.CharField('도착 지역', max_length=100)
    extra_distance = models.IntegerField('추가 거리', help_text='회기 시 추가로 산정될 거리')
    use_yn = models.BooleanField('사용여부', default=True)


class ChargeType(models.Model):
    section = models.ForeignKey(TransportSection, verbose_name='화물', on_delete=models.CASCADE, related_name='charge_types')
    truck = models.CharField('요금산정 우선순위', choices=TruckType.choices, max_length=20)
    per_km_cost = models.IntegerField('km당 요금')


class ChargeCalculator(models.Model):

    freight_name = models.CharField('화물명', max_length=128)
    load_weight = models.IntegerField('적재중량')
    chargeType = models.ForeignKey(ChargeType, verbose_name='금액산정 방식', on_delete=models.CASCADE)
    start_point = models.CharField('출발지', max_length=128)
    arrival_point = models.CharField('도착지', max_length=128)
    distance = models.IntegerField('거리')
    cost = models.IntegerField('운송비용')
