from django import forms
from deposits.models import Deposit


class AddDepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = [
            'deposit',
            'term',
            'rate',
        ]
