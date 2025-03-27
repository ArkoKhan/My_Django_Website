from django import forms
from .models import *


class ResumeHeadForm(forms.ModelForm):
    class Meta:
        model = ResumeHead
        fields = ["name", "occupation" , "dob", "image", "summary", "address", "phone"]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
        }



class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = ResumeEducation
        fields = ["degree", "institute", "start_year", "end_year"]


class ResumeExperienceForm(forms.ModelForm):
    class Meta:
        model = ResumeExperience
        fields = ["title", "company", "start_year", "end_year"]



class ResumeSkillForm(forms.ModelForm):
    class Meta:
        model = ResumeSkill
        fields = ["skill", "level"]




class LocationForm(forms.Form):
    city = forms.CharField(
        label="Location",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

class LocationReverseForm(forms.Form):
    lat = forms.FloatField(
        label="Latitude",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    lon = forms.FloatField(
        label="Longitude",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
