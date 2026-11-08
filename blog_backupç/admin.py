@'
from django.contrib import admin
from .models import Articulo

admin.site.register(Articulo)
'@ | Out-File -Encoding utf8 .\blog\admin.py