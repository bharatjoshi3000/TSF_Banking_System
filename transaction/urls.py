from django.contrib import admin
from django.urls import path
from transaction import views

app_name='transaction'

urlpatterns = [
    path('',views.home,name= 'home'),
    path('customers',views.customers,name= 'customers'),
    # path('transfer',views.transfer,name= 'transfer'),
    path('transop',views.transop,name= 'transop'),
    path('transaction_table',views.transaction_table,name= 'transaction_table'),
    
]
