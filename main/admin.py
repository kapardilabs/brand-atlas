from django.contrib import admin
from .models import *


# Register your models here.
class ConfigAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


admin.site.register(CrawlConfig, ConfigAdmin)
admin.site.register(Country)
admin.site.register(Brand)
