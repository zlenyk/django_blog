from django import forms

class FactorForm(forms.Form):
    integer = forms.CharField(label='Number to Factor', max_length=50)
