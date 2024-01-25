from django.contrib import admin
from .models import BOOKS_TBL,ORDERS_TBL

# Register your models here.
admin.site.register(BOOKS_TBL)
admin.site.register(ORDERS_TBL)