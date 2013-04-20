from django import forms

class GroupForm(forms.Form):
    '''Creates a form to add a group to application, containing the required fields.'''
    group_code = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=20)


class EmailForm(forms.Form):
    '''Creates a form to read the details to send emails to particular group.'''
    subject = forms.CharField(max_length=20)
    body = forms.CharField(max_length=1000)
    from_id = forms.EmailField()
    
