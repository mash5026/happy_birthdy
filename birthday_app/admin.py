from django.contrib import admin
from .models import *
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from django_jalali.admin.filters import JDateFieldListFilter


# Register your models here.

class PersonAdmin( ImportExportModelAdmin, ForeignKeyAutocompleteAdmin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_jalali_date_of_birth' ,'activity_unit', 'specilization', 'mobile_number', 'ad_date_of_birth')
    list_filter = ('last_name', ('date_of_birth', JDateFieldListFilter))
    def get_jalali_date_of_birth(self, obj):
                return obj.date_of_birth.strftime('%Y/%m/%d')
    get_jalali_date_of_birth.short_description="تاریخ تولد"

admin.site.register(Person, PersonAdmin)


class BirthdayMessageAdmin( ImportExportModelAdmin, ForeignKeyAutocompleteAdmin, admin.ModelAdmin):
    list_display = ('month_of_birth', 'message')
    list_filter = ('month_of_birth',)


admin.site.register(BirthdayMessage, BirthdayMessageAdmin)