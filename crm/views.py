from django.shortcuts import render

from cms.models import CmsSlider
from price.models import PriceCard
from telegrambot.sendmessage import send_telegram_message
from .forms import OrderForm
from .models import Order


def index(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)

    form = OrderForm()

    context = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'form': form,
    }
    return render(request, 'index.html', context)


def thanks(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        item = Order.objects.create(order_name=name, order_phone=phone)

        send_telegram_message(tg_name=name, tg_phone=phone)

        context = {
            'name': name,
            'phone': phone,
            'item': item,
        }
        return render(request, 'thanks.html', context)
    else:
        return render(request, 'thanks.html')
