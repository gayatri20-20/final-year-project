from dataclasses import fields
from random import choices
from tkinter import Label
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']

class DateInput(forms.DateInput):
    input_type = 'date'        

class HomeworkForm(forms.ModelForm):
    class Meta:
        model= Homework
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']


class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="Enter Your Search : ")

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']   
        
class ConversionForm(forms.Form):
    choices=[('length','Length'),('mass','Mass')]
    measurement=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)  

class ConversionLengthForm(forms.Form):
    choices= [('yard','Yard'),('foot','Foot')]   
    input= forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type': 'number','placeholder': 'Enter the NUmber'}
    ))  
    measure1= forms.CharField(
        label='',widget= forms.Select(choices=choices)
    )
    measure2= forms.CharField(
        label='',widget= forms.Select(choices=choices)
    )
class ConversionMassForm(forms.Form):
    choices= [('pound','Pound'),('kilogram','Kilogram')]   
    input= forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type': 'number','placeholder': 'Enter the NUmber'}
    ))  
    measure1= forms.CharField(
        label='',widget= forms.Select(choices=choices)
    )
    measure2= forms.CharField(
        label='',widget= forms.Select(choices=choices)
    )
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1','password2']
