from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Client,ClientExpense
from django.contrib import messages

import logging
import datetime

logger = logging.getLogger(__name__)

# Create your views here.

def listClientNames(request):
    try:
        if request.method == "GET":
            client = Client.objects.all()
            print(client)
            return render_to_response('expenses/listClientNames.html',context = {'client' : client })
    except Exception as e:
        logger.exception(e)

def listClientExpenses(request,client_name):
    try:
        if request.method == "GET":
            print(client_name)
            expenses = ClientExpense.objects.filter(client=client_name)
            print(expenses)
            return render_to_response('expenses/listClientExpenses.html',context={"expenses" :expenses,"client_name": client_name} )
    except Exception as e:
        logger.exception(e)
        
def addClient(request):
    try:
        if request.method == "POST":
            print(request.POST)
            clientInst = Client(name = request.POST.get('name'))
            clientInst.save()
            return HttpResponseRedirect(reverse('ClientNames'))
        elif request.method == "GET":
            return render(request,'expenses/addClient.html')
    except Exception as e:
        messages.error(request,'Something went wrong!')
        logger.exception(e)
        return render(request,'expenses/addClient.html')
def addExpense(request,client_name):
    try:
        if request.method == "POST":
            clientExpenseInst =  ClientExpense()
            clientExpenseInst.client_id = client_name
            clientExpenseInst.timestampOfExpense = datetime.datetime.now
            clientExpenseInst.title = request.POST.get('title')
            clientExpenseInst.description = request.POST.get('description')
            clientExpenseInst.expense_currency = request.POST.get('expense_currency')
            clientExpenseInst.expense = request.POST.get('expense')
            
            clientExpenseInst.save()
            return HttpResponseRedirect(reverse('ClientExpenses', args=[client_name]))
        elif request.method == "GET":
            #print("client_name:",client_name)
            return render(request,'expenses/addExpense.html',context={"client_name":client_name})
    except Exception as e:
        messages.error(request,'Something went wrong!')
        logger.exception(e)
        return render(request,'expenses/addExpense.html',context={"client_name":client_name})

