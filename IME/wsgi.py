
import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IME.settings")
application = DjangoWhiteNoise(application)