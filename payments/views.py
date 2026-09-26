import razorpay

from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from tournaments.models import Registration

client=razorpay.Client(
auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET)
)

def create_order(request):

    amount=5000

    order=client.order.create({
        "amount":amount,
        "currency":"INR",
        "payment_capture":1
    })

    return JsonResponse(order)

@csrf_exempt
def webhook(request):

    payload=json.loads(request.body)

    if payload["event"]=="payment.captured":

        order_id=payload["payload"]["payment"]["entity"]["order_id"]

        try:

            reg=Registration.objects.get(order_id=order_id)

            reg.paid=True

            reg.save()

        except:

            pass

    return HttpResponse(status=200)
