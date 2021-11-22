from django import forms

class PaymentForm(forms.Form):
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-phone_no', 'name':'form-phone_no', 'placeholder':'Phone Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'form-email', 'name':'form-email', 'placeholder':'Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))#Provide some choices for the address to be entered



class SearchForm(forms.Form):
    choices = (('Reference', 'Reference Code'), ('Owner', 'Owner'))
    select = forms.CharField(widget=forms.Select(choices=choices))
    search_text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-name', 'name':'form-name', 'placeholder':'Search products...'}))
