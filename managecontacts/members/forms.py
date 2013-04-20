from django import forms

class MemberForm(forms.Form):
    '''Creates a form to create add anew member.'''
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    dob = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=20)
    organisation = forms.CharField(max_length=20)
    email = forms.EmailField()


class UploadFileForm(forms.Form):
    '''Create a form to upload an excel or zip file containing the data to be read and updated.'''
    title = forms.CharField(max_length=20)
    file  = forms.FileField()