from ejeevanprateek.models import Contact, Parameter
from django import forms

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"

class ParameterForm(forms.ModelForm):
    
    class Meta:
        model = Parameter
        fields = "__all__"