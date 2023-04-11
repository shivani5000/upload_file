from django import forms
from .models import indexmail,detailmail1

class FormContactForm(forms.ModelForm):#FormContactForm is the name of the class of form.py
    class Meta:
        model= indexmail
        fields= ["email"]    
        
class FormContact(forms.ModelForm):#FormContactForm is the name of the class of form.py
    class Meta:
        model= detailmail1
        fields= ["name","email1","date","time","person"]            