# Create your models here.
from django.db import models

from apps.calculator.enums import TruckType


class TransportSection(models.Model):

    class Meta:
        verbose_name = '이동구간'

    start_area = models.CharField('출발 지역', max_length=100)
    arrival_area = models.CharField('도착 지역', max_length=100)
    extra_distance = models.IntegerField('추가 거리', help_text='회기 시 추가로 산정될 거리')
    is_use = models.BooleanField('사용여부', default=True)
    create_dt = models.DateTimeField('생성일', auto_now_add=True)
    update_dt = models.DateTimeField('수정일', auto_now=True)

class ChargeType(models.Model):

    class Meta:
        verbose_name = '요금산정 방식'

    section = models.ForeignKey(TransportSection, verbose_name='화물', on_delete=models.CASCADE, related_name='charge_types')
    truck = models.CharField('화물차종', choices=TruckType.choices, max_length=20)
    per_km_cost = models.IntegerField('km당 요금')
    create_dt = models.DateTimeField('생성일', auto_now_add=True)
    update_dt = models.DateTimeField('수정일', auto_now=True)


class ChargeCalculator(models.Model):

    chargeType = models.ForeignKey(ChargeType, verbose_name='요금산정 방식', on_delete=models.CASCADE)
    freight_name = models.CharField('화물명', max_length=128)
    load_weight = models.IntegerField('적재중량')
    start_point = models.CharField('출발지', max_length=128)
    arrival_point = models.CharField('도착지', max_length=128)
    distance = models.IntegerField('거리')
    cost = models.IntegerField('운송비용')
    create_dt = models.DateTimeField('생성일', auto_now_add=True)
    update_dt = models.DateTimeField('수정일', auto_now=True)