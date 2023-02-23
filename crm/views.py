from django.shortcuts import render

from .models import Order
from .forms import OrderForm


def index(request):
    orders = Order.objects.all()
    form = OrderForm()
    return render(request, 'index.html', {'orders': orders,
                                              'form': form})


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
