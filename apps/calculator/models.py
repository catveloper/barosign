from django.db import models

# Create your models here.
from django.db import models

from apps.calculator.enums import ChargeType


class Freight(models.Model):

    name = models.CharField('화물명', max_length=100, unique=True)
    priority = models.CharField('요금산정 우선순위', choices=ChargeType.choices, max_length=20, help_text='어떤 항목을 요금 산정의 1차 기준으로 설정할지')
    rate_conversion_point = models.IntegerField('요금산정 전환 기준점', help_text='우선순위로 선택한 무게 또는 부피가 얼마 이상일 때 기준을 변경할지')
    charge_per_weight = models.IntegerField('무게당 금액')
    charge_per_volume = models.IntegerField('부피당 금액')
    create_dt = models.DateTimeField('작성일', auto_now_add=True)
    update_dt = models.DateTimeField('수정일', auto_now=True)


class ChargeCalculator(models.Model):
    pass