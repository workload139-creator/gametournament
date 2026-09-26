import json
import razorpay

from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tournaments.models import Registration
from .models import Payment

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET)
)

def create_order(request):

    amount = 5000

    order = client.order.create({
        "amount":amount,
        "currency":"INR",
        "payment_capture":1
    })

    Payment.objects.create(
        user=request.user,
        order_id=order["id"],
        amount=amount
    )

    return JsonResponse(order)

@csrf_exempt
def webhook(request):

    payload = json.loads(request.body)

    if payload["event"]=="payment.captured":

        entity = payload["payload"]["payment"]["entity"]

        order_id = entity["order_id"]

        payment_id = entity["id"]

        try:

            payment = Payment.objects.get(order_id=order_id)

            payment.payment_id = payment_id

            payment.verified = True

            payment.save()

            Registration.objects.filter(
                player=payment.user
            ).update(
                paid=True,
                order_id=order_id
            )

        except Payment.DoesNotExist:
            pass

    return HttpResponse(status=200)
