from django import forms

class InputForm(forms.Form):
    prompt = forms.CharField(
        label='Prompt',
        max_length=1500,
        widget=forms.TextInput(attrs={ "class": "form-control" })
    )



class DeepAiInputForm(forms.Form):
    CHOICES = {
        ('chat', 'Chat'),
        ('image', 'Image')
    }
    model = forms.ChoiceField(
        label='Model',
        choices=CHOICES,
        widget=forms.Select(attrs={ "class": "form-control" })
    )
    prompt = forms.CharField(
        label='Prompt',
        max_length=1500,
        widget=forms.TextInput(attrs={ "class": "form-control" })
    )