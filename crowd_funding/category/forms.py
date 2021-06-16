from django import forms
import datetime
class Category_form(forms.Form):
    name = forms.CharField(label=False, max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Add category name',
                                                         }))
