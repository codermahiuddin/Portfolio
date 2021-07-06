from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ('name','email','subject','msg')
    
    widgets = {
        'name' : forms.TextInput(attrs={'class' : 'form-control'})
    }