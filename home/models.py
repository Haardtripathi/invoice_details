from django.db import models

# Create your models here.
class Invoice(models.Model):
    date=models.DateField(auto_now_add=True)
    customer_name=models.CharField(max_length=100)
    def __str__(self):
        return self.customer_name
    

class InvoiceDetails(models.Model):
    invoice=models.ForeignKey(Invoice, related_name="invoice",on_delete=models.CASCADE)
    description=models.TextField(max_length=300)
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    price=models.IntegerField()
    def __str__(self):
        return self.invoice.customer_name
