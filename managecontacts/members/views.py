import os
import sys
import xlrd
import glob
import zipfile
import datetime

from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from groups.models import Group
from members.models import Member
from managecontacts.settings import PROJECT_ROOT
from members.forms import MemberForm, UploadFileForm


def member(request):
    '''Creates a view to add members to database, if the group code exists,\
    add the user to that group or else create a new group and save.'''
    members = Member.objects.all()
    groups = Group.objects.all() 
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            organisation = form.cleaned_data['organisation']
            email = form.cleaned_data['email']
            options = request.POST.getlist('group')
            new_code = request.POST['new_group']
            name = request.POST['name']
            description = request.POST['description']
            try:
                member = Member()
                member.firstname = firstname
                member.lastname = lastname
                member.dob = dob
                member.gender = gender
                member.organisation = organisation
                member.email = request.POST['email']
                grp_codes = [str(x) for x in options]
                for cd in grp_codes:
                    if cd:
                        gr = Group.objects.get(group_code = cd)
                        member.group = gr
                g, status = Group.objects.get_or_create(group_code=new_code)
                g.name = name
                g.description = description
                member.group = g
                member.save()
            except:
                pass
            return HttpResponseRedirect(reverse('index'))
    else:
        form = MemberForm()
    context = {'members' : members, 'groups' : groups, 'form':form}
    return render(request, 'members/member.html', context )

def upload_file(request):
    '''Creates a view to upload a file and read the contents, if the uploaded file is\
    a zip file, file is first extracted and read. the file is read and updates the data\
    to database. if the corresponding group is not present, a new group is created and updated.'''
    x = {}
    y = []
    s = []
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.files['file']
            filename = str(title)
            x = request.FILES
            front=filename.split('.')[0]
            if filename.endswith('.zip'):
                zipf = zipfile.ZipFile(x['file'])
                zipf.extractall(os.getcwd())
            else:
                y = x['file'].read()
            z=''+ front + '.xlsx'
            path = default_storage.save(z, ContentFile(y))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            if form.is_valid():
                workbook = xlrd.open_workbook(z)
                sh = workbook.sheet_by_name('Sheet1')
                for rownum in range(sh.nrows):
                    member = Member()
                    member.firstname = sh.row_values(rownum)[0]
                    member.lastname = sh.row_values(rownum)[1]
                    member.dob = sh.row_values(rownum)[2]
                    member.gender = sh.row_values(rownum)[3]
                    member.organisation = sh.row_values(rownum)[4]
                    member.email = sh.row_values(rownum)[5]
                    code =  str(sh.row_values(rownum)[6])
                    group, status = Group.objects.get_or_create(group_code=code)
                    member.group = group
                    member.save()
                    
                os.chdir(os.getcwd())
                files=glob.glob('*.xlsx')
                for filename in files:
                    os.unlink(filename)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render(request, 'contacts/read.html', {'form': form})
