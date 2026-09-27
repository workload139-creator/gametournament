import requests
from django.conf import settings

def send_whatsapp(phone,message):

    url=f"https://graph.facebook.com/v20.0/{settings.WHATSAPP_PHONE_ID}/messages"

    headers={
        "Authorization":f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type":"application/json"
    }

    data={
        "messaging_product":"whatsapp",
        "to":phone,
        "type":"text",
        "text":{
            "body":message
        }
    }

    try:
        requests.post(url,json=data,headers=headers,timeout=10)
    except:
        pass
