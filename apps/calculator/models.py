# Create your models here.
from django.db import models

from apps.calculator.enums import ChargeType


class Freight(models.Model):

    name = models.CharField('화물명', max_length=100, unique=True)
    priority = models.CharField('요금산정 우선순위', choices=ChargeType.choices, max_length=20, help_text='어떤 항목을 요금산정의 1차 기준으로 설정할지')
    rate_conversion_point = models.IntegerField('요금기준 전환점', help_text='우선순위로 선택한 무게 또는 부피가 얼마 이상일 때 요금기준을 변경할지')
    charge_per_weight = models.IntegerField('무게당 금액')
    charge_per_volume = models.IntegerField('부피당 금액')
    is_use = models.BooleanField('사용여부', default=True)
    create_dt = models.DateTimeField('작성일', auto_now_add=True)
    update_dt = models.DateTimeField('수정일', auto_now=True)

    def get_priority_unit_html(self):
        return ChargeType[self.priority].unit_html


class ChargeCalculator(models.Model):

    freight = models.ForeignKey(Freight, on_delete=models.CASCADE)
    start_point = models.CharField('출발점')
    arrival_point = models.CharField('출발점')
    distance = models.IntegerField('거리')
