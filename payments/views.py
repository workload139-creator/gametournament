import razorpay
import json

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

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

    data = json.loads(request.body)

    if data["event"] == "payment.captured":
        pass

    return HttpResponse(status=200)
