from django import forms

class JobSearchForm(forms.Form):

    # on site, remote, hybrid

    CHOICES = {
        ('on site', 'on site'),
        ('remote', 'remote'),
        ('hybrid', 'hybrid'),
    }
    job_title = forms.CharField(
        label='Job Title',
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    location = forms.CharField(
        label='Location',
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    remote_filter = forms.ChoiceField(
        label='Remote Filter',
        choices=CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )