import hmac
import hashlib
import json

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tournaments.models import Registration

@csrf_exempt
def razorpay_webhook(request):

    signature = request.headers.get("X-Razorpay-Signature","")

    body = request.body

    expected = hmac.new(
        settings.RAZORPAY_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if signature != expected:
        return HttpResponse(status=400)

    payload = json.loads(body)

    if payload["event"]=="payment.captured":

        order = payload["payload"]["payment"]["entity"]["order_id"]

        Registration.objects.filter(order_id=order).update(paid=True)

    return HttpResponse(status=200)
