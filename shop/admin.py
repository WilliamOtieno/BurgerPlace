from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','location','totalp')

admin.site.register(Order, OrderAdmin)