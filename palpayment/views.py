from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from django.urls import reverse, reverse_lazy
from paypal.standard.forms import PayPalPaymentsForm

from django.views.decorators.csrf import csrf_exempt

from app.models import Reservation
from .models import *
from app.forms import ReservationForm

# Create your views here.

def checkout(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
        #...
        #...

            form.clear(request)

            request.session['order_id'] = Reservation.id
            return redirect('process_payment')

    else:
        form = ReservationForm()
        return render(request, 'ecommerce_app/checkout.html', locals())


def process_payment(request):
    reservation_id = request.session.get('reservation_id')
    reservation = get_object_or_404(reservation, id=reservation_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % reservation.total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(reservation.id),
        'invoice': str(reservation.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'ecommerce_app/process_payment.html', {'order': reservation, 'form': form})


def process_payment(request):
    pass


@csrf_exempt
def payment_done(request):
    return render(request, 'ecommerce_app/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'ecommerce_app/payment_cancelled.html')
