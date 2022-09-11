from django.contrib import admin
from django.contrib.auth import get_user_model
from records.models import Records


admin.site.register(Records)
