from django.contrib import admin
from django.apps import apps
from .models import *

# Get all models from the current app
app_models = apps.get_app_config('chat').get_models()

# Register each model dynamically
for model in app_models:
    admin.site.register(model)

