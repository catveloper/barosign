from django.db import models

# Create your models here.
from django.db import models

from apps.calculator.enums import PriceType


class Freight(models.Model):

    name = models.CharField(verbose_name='화물명', max_length=100, unique=True)
    priority = models.CharField(verbose_name='우선순위', help_text='금액을 적용할 우선순위', choices=PriceType.choices, max_length=20)
    price_per_weight = models.IntegerField(verbose_name='무게당 금액')
    price_per_volume = models.IntegerField(verbose_name='부피당 금액')
