import razorpay
import json

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tournaments.models import Registration

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET)
)

def create_order(request):

    order = client.order.create({
        "amount": 5000,
        "currency": "INR",
        "payment_capture": 1
    })

    return JsonResponse(order)

@csrf_exempt
def webhook(request):

    payload = json.loads(request.body)

    if payload["event"] == "payment.captured":

        order_id = payload["payload"]["payment"]["entity"]["order_id"]

        try:

            registration = Registration.objects.get(order_id=order_id)

            registration.paid = True

            registration.save()

        except Registration.DoesNotExist:
            pass

    return HttpResponse(status=200)
