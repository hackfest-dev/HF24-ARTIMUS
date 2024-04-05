from django.db import models



class Delivery(models.Model):
    delivery_address = models.CharField(max_length=200, help_text='Enter the delivery address')
    delivery_time = models.DateTimeField(help_text='Enter the delivery time')
    delivery_person_name = models.CharField(max_length=100, help_text='Enter the delivery person name')
    company_name = models.CharField(max_length=100, help_text='Enter the company name')
    item_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter the item price')
    status = models.CharField(max_length=20, help_text='Enter the status of the delivery')
    sender_address = models.CharField(max_length=200, help_text='Enter the sender address')
    is_paid = models.BooleanField(default=False, help_text='Specify if the delivery is paid or not')

    def __str__(self):
        return f"Delivery #{self.pk}: {self.delivery_address} - {self.delivery_time}"
    



