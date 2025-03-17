from django import forms
from .models import Bid

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'مبلغ پیشنهادی (تومان)', 'min': '1'})
        }