INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "teams",
    "wallet",
    "referrals",
    "accounts",
    "tournaments",
    "payments",
    "leaderboard",
]

AUTH_USER_MODEL = "accounts.User"

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]

RAZORPAY_KEY = "rzp_test_xxxxx"
RAZORPAY_SECRET = "xxxxxxxx"

WHATSAPP_TOKEN = "YOUR_META_ACCESS_TOKEN"
WHATSAPP_PHONE_ID = "YOUR_PHONE_NUMBER_ID"


