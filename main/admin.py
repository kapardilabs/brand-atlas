from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass
