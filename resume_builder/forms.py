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
        label="City",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
