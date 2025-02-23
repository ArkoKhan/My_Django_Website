from django import forms
from django_ckeditor_5.fields import CKEditor5Widget

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    message = forms.CharField(
        label='Your Message',
        widget=CKEditor5Widget(attrs={'class': 'form-control', 'placeholder': 'Your Message'}, config_name="default")
    )