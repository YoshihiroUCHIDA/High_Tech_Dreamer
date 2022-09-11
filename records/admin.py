from django.contrib import admin
from django.contrib.auth import get_user_model
from records.models import Record


admin.site.register(Record)
