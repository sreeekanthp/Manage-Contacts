import datetime

from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from contracts.models import Contract 
from contracts.forms import ContractForm

def contract(request):
    '''Creates a view to save the contract details.'''
    contracts = Contract.objects.all() 
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            list_size = form.cleaned_data['list_size']
            total_email = form.cleaned_data['total_email']
            try:
                contract = Contract()
                contract.from_date = from_date
                contract.to_date = to_date
                contract.list_size = list_size
                contract.total_email = total_email
                contract.save()
            except:
                pass
                
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ContractForm()
    context = {'contracts' : contracts, 'form' : form}
    return render(request, 'contracts/contract.html', context )
