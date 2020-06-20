from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(CrawlConfig)
class ConfigAdmin(ImportExportModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    pass
