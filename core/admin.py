from django.contrib import admin
from django.contrib.auth.models import Permission


# Register your models here.
from .models import Blog

admin.site.register(Blog)
