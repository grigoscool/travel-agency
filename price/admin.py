from django.contrib import admin

from .models import PriceCard, PriceTable


class PriceTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'pt_title', 'pt_new_price')
    list_display_links = ('id', 'pt_title')



admin.site.register(PriceCard)
admin.site.register(PriceTable, PriceTableAdmin)