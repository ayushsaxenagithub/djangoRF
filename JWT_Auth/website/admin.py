from django.contrib import admin
from .models import CustomToken
from rest_framework.authtoken.models import Token

# Register your models here.


admin.site.register(CustomToken)
admin.site.register(Token)
