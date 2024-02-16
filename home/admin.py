from django.contrib import admin
from .models import *
# Register your models here.
class InvoiceDetailsAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name', 'description')

    def get_customer_name(self, obj):
        return obj.invoice.customer_name
    get_customer_name.short_description = 'Customer Name'  # Sets column name

admin.site.register(Invoice)  # Register Invoice model as well if not already done
admin.site.register(InvoiceDetails, InvoiceDetailsAdmin)