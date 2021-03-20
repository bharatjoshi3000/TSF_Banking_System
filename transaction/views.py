from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Transaction

template_name = 'transactions.html'

# Create your views here.
def home(request):
    return render(request,"index.html")
    # return HttpResponse("hello world")

def customers(request):
    custs = Customer.objects.all()
    return render(request, "customers.html",{'data':custs})


# def transfer(request):
#     custs = Customer.objects.all()
#     return render(request,"transactions.html",{'data':custs})

def transop(request):
    if request.method == 'POST':
        cred_to = request.POST["transfer_to"]
        debt_from = request.POST["transfer_from"]
        amount = request.POST["amount"]
        try:
            receiver = Customer.objects.get(name=cred_to)
            sender = Customer.objects.get(name=debt_from)
            amount = int(amount)
            if amount <= sender.balance:
                sender.balance -= amount
                receiver.balance += amount
                sender.save()
                receiver.save()
                new_txn = Transaction(debited_from=sender, credited_to=receiver , amount=amount,transaction_status="SUCCESS")
                new_txn.save()
                data = Transaction.objects.all().order_by('-transaction_date')
                print("reached here")
                context = {'data':data,'message':"Transaction successful."}
                return render(request,"transactions.html",context)

            else:
                new_txn=Transaction(
                    debited_from=sender, credited_to=receiver,amount=amount,transaction_status="FAILED"
                )
                new_txn.save()
                return render(request,template_name,{"error":"Your account doesn't have sufficient balance"})
        except Customer.DoesNotExist:
            return render(request,template_name,{"error":"Account Number does not match with any customer"})
    else:
        return render(request,template_name)

def transaction_table(request):
    data = Transaction.objects.all().order_by('-transaction_date')
    context = {'data':data}
    return render(request,"transactions.html",context)

