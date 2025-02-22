from django import forms

class InputForm(forms.Form):
    prompt = forms.CharField(
        label='Prompt',
        max_length=1500,
        widget=forms.TextInput(attrs={ "class": "form-control" })
    )