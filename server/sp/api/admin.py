from django.contrib import admin
from .models import Citizen, Alert#,

# Register your models here.

admin.site.register(Citizen)
admin.site.register(Alert)