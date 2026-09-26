INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "accounts",
    "tournaments",
    "payments",
    "leaderboard",
]

AUTH_USER_MODEL = "accounts.User"

STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]

RAZORPAY_KEY = "rzp_test_xxxxx"
RAZORPAY_SECRET = "xxxxxxxx"
