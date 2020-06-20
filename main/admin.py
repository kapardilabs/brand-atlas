from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class ConfigAdmin(ImportExportModelAdmin):
    resource_class = CrawlConfig


class BrandAdmin(ImportExportModelAdmin):
    resource_class = Brand


class CountryAdmin(ImportExportModelAdmin):
    resource_class = Country


admin.site.register(CrawlConfig, ConfigAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Brand, BrandAdmin)
