from django.urls import path
from .views import create_order,webhook

urlpatterns = [

    path("create-order/",create_order,name="create_order"),

    path("webhook/",webhook,name="payment_webhook"),

]
