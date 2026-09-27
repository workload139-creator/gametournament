import requests
from django.conf import settings

def send_whatsapp(phone,message):

    requests.post(

    f"https://graph.facebook.com/v20.0/{settings.WHATSAPP_PHONE_ID}/messages",

    headers={
    "Authorization":f"Bearer {settings.WHATSAPP_TOKEN}"
    },

    json={
    "messaging_product":"whatsapp",
    "to":phone,
    "type":"text",
    "text":{"body":message}
    }

    )
