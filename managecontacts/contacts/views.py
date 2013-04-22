import datetime

from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from contacts.models import Contact 
from contacts.forms import ContactForm
from contracts.models import Contract
from members.models import Member
from groups.models import Group

def index(request):
    '''Creates the view of index page.'''
    return render(request, 'contacts/index.html')


def contact(request):
    '''Creates a view for adding contact, and saves the new contact to database.'''
    contacts = Contact.objects.all()
    contracts = Contract.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            options = request.POST.getlist('contract')
            try:
                contact = Contact()
                contact.firstname = firstname
                contact.lastname = lastname
                contact.email = email
                contract_dates = [str(x) for x in options]
                for cd in contract_dates:
                    if cd:
                        cr = Contract.objects.get(from_date = cd)
                        contact.contract = cr
                contact.save()
            except:
                pass

            return HttpResponseRedirect(reverse('index'))
        
    else:
        form = ContactForm()

    context = {'contacts' : contacts, 'contracts': contracts, 'form' :form}
    return render(request, 'contacts/contact.html', context )
