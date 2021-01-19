from .models import *
from django import forms


class RequestForm(forms.ModelForm):
    content = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Написать', 'rows': 1, 'cols': 3}))

    class Meta:
        model = Requests
        fields = ('content',)