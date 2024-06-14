from django.contrib import admin

from cars.models import Brand, Car


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "factory_year", "model_year", "value")
    search_fields = ("model", "brand")


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
