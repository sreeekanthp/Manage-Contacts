from django import forms

class ContactForm(forms.Form):
    '''Creates a form for the application to add a contact. '''
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email = forms.EmailField()
