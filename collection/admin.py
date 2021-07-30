from django.contrib import admin

from .models import Collection, APIRequest


admin.site.register(Collection)
admin.site.register(APIRequest)
