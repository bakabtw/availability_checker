from django.contrib import admin
from .models import Host, Method, Status

admin.site.register(Host)
admin.site.register(Method)
admin.site.register(Status)
