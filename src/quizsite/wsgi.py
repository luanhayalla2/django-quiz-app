"""
WSGI config for quizsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

# Add the 'src' directory to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quizsite.settings")

application = get_wsgi_application()
app = application

