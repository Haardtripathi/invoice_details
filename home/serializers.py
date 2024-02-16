from rest_framework import serializers
from .models import *

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields="__all__"
    
class InvoiceDetailsSerializer(serializers.ModelSerializer):
    invoice=InvoiceSerializer()
    class Meta:
        model=InvoiceDetails
        fields = "__all__" 
    def create(self, validated_data):
        invoice_data = validated_data.pop('invoice')
        try:
            invoice, created = Invoice.objects.get_or_create(**invoice_data)
        except MultipleObjectsReturned:
            invoice = Invoice.objects.filter(**invoice_data).first()  # Or use another strategy to select the correct invoice
            created = False  # Since we're fetching an existing instance, not creating a new one
        
        invoice_details = InvoiceDetails.objects.create(invoice=invoice, **validated_data)
        return invoice_details