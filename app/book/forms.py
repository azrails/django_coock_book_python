from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Ingridient, Recipe
from django.contrib.auth.models import User
from django.utils import timezone


class filter_ingridient(forms.Form):
    INGR = []
    tmp = []
    try:
        ingridients = Ingridient.objects.all().order_by('title')
        for ingridient in ingridients:
            INGR.append((ingridient.pk, ingridient.title),)
        value = forms.ChoiceField(label='', choices=INGR, widget=forms.Select(attrs={'class': 'form-select indent'}))
    except:
        INGR.append(())
        value = forms.ChoiceField(label='', choices=INGR, widget=forms.Select(attrs={'class': 'form-select indent'}))

class search_recipe(forms.Form):
    value = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class': 'form-control indent', 'placeholder': 'Search recipe'}))


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control indent', 'placeholder': 'Enter Login', 'label': '', 'help_text': '', 'label-suffix': ''})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control indent', 'placeholder': 'Enter Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control indent', 'placeholder': 'Enter Email'})

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control indent', 'placeholder': 'Enter Username'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control indent', 'placeholder': 'Enter Username'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class': 'form-control indent', 'placeholder': 'Enter Username'}))
    password = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class': 'form-control indent', 'placeholder': 'Enter Password'}))


class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'formula', 'ingridients')


class CreateIngridient(forms.ModelForm):
    class Meta:
        model = Ingridient
        fields = ('title',)