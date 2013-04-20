import datetime

from django import forms
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from groups.models import Group
from groups.forms import GroupForm, EmailForm
from members.models import Member


def group(request):
    '''Creates a view of group to add a new group reading the user posted data.'''
    groups = Group.objects.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_code = form.cleaned_data['group_code']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            try:
                group = Group()
                group.group_code = group_code
                group.name = name
                group.description = description
                group.save()
            except:
                pass
            return HttpResponseRedirect(reverse('index'))
    else:
        form = GroupForm()
    return render(request, 'groups/group.html', {'groups' : groups, 'form' : form} )

def email(request,group_id):
    '''Creates a view to send emails to a group,the address of the group members are\
    append to a list and read subject and body of email is send to the list.'''
    add = []
    group = Group.objects.get(id=group_id)
    members = group.member_set.all()
    for member in members:
        add.append(member.email)
    addr_list  = [str(x) for x in add]
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject =form.cleaned_data['subject']
            body = form.cleaned_data['body']
            from_id = form.cleaned_data['from_id']
            try:
                subject = str(subject)
                body = str(body)
                from_id = str(from_id)
                send_mail(subject, body, from_id, addr_list, fail_silently=False)
            except:
                pass
            return HttpResponseRedirect(reverse('index'))

    else:
        form = EmailForm()
    context = {'group': group,'members' :members, 'form' : form}
    return render(request, 'groups/email.html', context)
