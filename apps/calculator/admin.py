from django.contrib import admin

# Register your models here.
from apps.calculator.models import TransportSection


@admin.register(TransportSection)
class TransportSectionAdmin(admin.ModelAdmin):
    pass