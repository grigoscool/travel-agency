from django.shortcuts import render

from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider


def index(request):
    slider_list = CmsSlider.objects.all()
    return render(request, 'index.html', {'slider_list': slider_list})


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    item = Order.objects.create(order_name=name, order_phone=phone)

    context = {
        'name': name,
        'phone': phone,
        'item': item,
    }
    return render(request, 'thanks.html', context)
