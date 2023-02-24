from django.shortcuts import render

from .models import Order
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from .forms import OrderForm
from telegrambot.sendmessage import send_telegram_message

def index(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)

    form = OrderForm()

    services = PriceTable.objects.all()
    context = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'services': services,
        'form': form,
    }
    return render(request, 'index.html', context)


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    item = Order.objects.create(order_name=name, order_phone=phone)

    send_telegram_message()

    context = {
        'name': name,
        'phone': phone,
        'item': item,
    }
    return render(request, 'thanks.html', context)
