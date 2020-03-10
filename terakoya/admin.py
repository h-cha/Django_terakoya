from django.contrib import admin

# Register your models here.

from .models import Input,Question

admin.site.register(Input)
admin.site.register(Question)