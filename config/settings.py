from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "CHANGE_ME"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "channels",

    "accounts",
    "tournaments",
    "teams",
    "payments",
    "wallet",
    "leaderboard",
    "referrals",
    "notifications",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
{
"BACKEND":"django.template.backends.django.DjangoTemplates",
"DIRS":[BASE_DIR/"templates"],
"APP_DIRS":True,
"OPTIONS":{
"context_processors":[
"django.template.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
]
}
}
]

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"

DATABASES = {
"default":{
"ENGINE":"django.db.backends.sqlite3",
"NAME":BASE_DIR/"db.sqlite3"
}
}

AUTH_PASSWORD_VALIDATORS=[]

LANGUAGE_CODE="en-us"

TIME_ZONE="Asia/Kolkata"

USE_I18N=True

USE_TZ=True

STATIC_URL="/static/"
STATICFILES_DIRS=[BASE_DIR/"static"]
STATIC_ROOT=BASE_DIR/"staticfiles"

MEDIA_URL="/media/"
MEDIA_ROOT=BASE_DIR/"media"

AUTH_USER_MODEL="accounts.User"

CHANNEL_LAYERS={
"default":{
"BACKEND":"channels.layers.InMemoryChannelLayer"
}
}

RAZORPAY_KEY="rzp_test_xxxxx"
RAZORPAY_SECRET="xxxxxxxx"

WHATSAPP_TOKEN="YOUR_META_TOKEN"
WHATSAPP_PHONE_ID="YOUR_PHONE_ID"
"config.middleware.MaintenanceMiddleware",
