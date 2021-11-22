from django import forms
from .models import Category, Product

class SearchForm(forms.Form):
    choices = (('Product', 'Product'), ('Category', 'Category'))
    select = forms.CharField(widget=forms.Select(choices=choices))
    search_text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-name', 'name':'form-name', 'placeholder':'Search products...'}))

class ReviewForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'name':'name', 'placeholder':'Name..'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'name':'email', 'placeholder':'Email..' }))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'subject', 'name':'phone', 'placeholder':'Subject..'}))
    review = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'6', 'id':'review', 'name':'review', 'placeholder':'Your Message Here...'})) 

