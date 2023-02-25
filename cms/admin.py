from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


class CmsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cms_title', 'cms_css', 'get_img')
    list_display_links = ('id', 'cms_title')
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_css', 'get_img', 'cms_img')
    readonly_fields = ('get_img', )

    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'Нет фото'

    get_img.short_description = 'Превью'


admin.site.register(CmsSlider, CmsAdmin)
