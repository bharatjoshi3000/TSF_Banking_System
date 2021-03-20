from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200)
    account_number = models.CharField(max_length=50)
    email=models.EmailField()
    city=models.CharField(max_length=100)
    balance=models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.name

    
class Transaction(models.Model):

    debited_from=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="sender")
    credited_to=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="receiver")
    amount=models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status=models.CharField(max_length=20, default="Pending")


    def get_transaction_by_sender(self, customer_id):
        return Transaction.objects.filter(debited_from=customer_id).order_by('-transaction_date')

    def get_transaction_by_receiver(self, customer_id):
        return Transaction.objects.filter(credited_to=customer_id).order_by('-transaction_date')
    
