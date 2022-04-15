from django.contrib import admin

from .models import Package


# Register your models here.
class PackageList(admin.ModelAdmin):
    list_display = ("pack_number", "location", "price", "start_date", "end_date", "rating",)
    list_filter = ('pack_number', 'price', 'start_date', 'end_date',)
    search_fields = ('pack_number', 'price', 'start_date', 'end_date',)
    ordering = ['pack_number']


admin.site.register(Package, PackageList)
