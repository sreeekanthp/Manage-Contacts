from django import forms


class ContractForm(forms.Form):
    '''Creates a form for adding contract containing From and To date\
    List size and Total emails that could be send etc. '''
    from_date = forms.DateField()
    to_date = forms.DateField()
    list_size = forms.IntegerField()
    total_email = forms.IntegerField()
