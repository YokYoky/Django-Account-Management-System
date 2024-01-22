from django import forms
from .models import Account

class accountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_number', 'email', 'first_name', 'last_name', 'sex', 'residence']
        labels = {
            'account_number': 'Account Number',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'sex': 'Sex',
            'residence': 'Residence'
        }
        widgets = {
        'account_number': forms.NumberInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'sex': forms.Select(attrs={'class': 'form-control'}),
        'residence': forms.TextInput(attrs={'class': 'form-control'}),
        }