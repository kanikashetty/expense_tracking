from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Client(models.Model):
    
    " Client models contains the name of the client"
    
    name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.name

class ClientExpense(models.Model):
   
    " This models defines the different fields of client's expenditure"
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    timestampOfExpense = models.DateTimeField(auto_now_add=True)
    CURRENCY_CHOICES = (
        ('INR','INR'),
        ('USD','USD')
    )
    expense = MoneyField(decimal_places=2, max_digits=8,currency_choices=CURRENCY_CHOICES)
    title = models.TextField()
    description = models.TextField(blank=True)

        
    
