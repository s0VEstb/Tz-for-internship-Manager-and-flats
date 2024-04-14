from django.contrib import admin
from .models import Apartment, Client


# Register your models here.
admin.site.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category',)
    list_editable = ('price', 'category')
    search_fields = ('title', 'category',)
    readonly_fields = ('id',)
    fields = ('title', 'price', 'category',)


admin.site.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'contract_number')
    list_editable = ('full_name', 'phone', 'contract_number')
    search_fields = ('contract_number', 'full_name',)
    readonly_fields = ('id',)
    fields = ('full_name', 'phone', 'contract_number')

