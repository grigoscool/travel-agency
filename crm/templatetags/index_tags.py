from django import template

from price.models import PriceTable
from cms.models import CmsSlider

register = template.Library()


@register.simple_tag(name='price_table')
def get_price_table():
    return PriceTable.objects.all()


@register.inclusion_tag('slider_list.html')
def get_slider_list():
    slider_list = CmsSlider.objects.all()
    return {'slider_list': slider_list}
