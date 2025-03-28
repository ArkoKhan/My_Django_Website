from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import HttpResponse
from my_website.renderers import render_to_pdf
from django.views.generic import View
from django.conf import settings
import os

# Create your views here.
class GeneratePDF(View):
    def get(self, request, username, *args, **kwargs):
        user = User.objects.get(username=username)
        cv = ResumeHead.objects.get(user=user)
        education = ResumeEducation.objects.filter(resume=cv)
        experience = ResumeExperience.objects.filter(resume=cv)
        skills = ResumeSkill.objects.filter(resume=cv)

        context = {
            "resume": cv,
            "education": education,
            "experience": experience,
            "skills": skills,
            "image_path" : "",
            "user" : user,
        }
        if cv.image:
            image_path = os.path.join(settings.MEDIA_ROOT, cv.image.name)
            context["image_path"] = image_path
            pdf = render_to_pdf('resume/download.html', context)
            return HttpResponse(pdf, content_type='application/pdf')

def resume(request, username):
    try:
        user = User.objects.get(username=username)
        cv = ResumeHead.objects.get(user=user)
        education = ResumeEducation.objects.filter(resume=cv)
        experience = ResumeExperience.objects.filter(resume=cv)
        skills = ResumeSkill.objects.filter(resume=cv)
        context = {
            "resume": cv,
            "education": education,
            "experience": experience,
            "skills": skills
        }
    except:
        messages.warning(request,"Resume does not exist")
        return redirect("create_resume")
    return render(request, 'resume/resume.html', context=context)

def download_resume(request, username):
    user = User.objects.get(username=username)
    cv = ResumeHead.objects.get(user=user)
    education = ResumeEducation.objects.filter(resume=cv)
    experience = ResumeExperience.objects.filter(resume=cv)
    skills = ResumeSkill.objects.filter(resume=cv)
    context = {
        "resume": cv,
        "education": education,
        "experience": experience,
        "skills": skills
    }
    return render(request, 'resume/download.html', context=context)

def create_resume(request):
    if ResumeHead.objects.filter(user=request.user).exists():
        messages.warning(request,"Resume already exists")
        return redirect('resume', username=request.user.username)
    else:
        if request.method == "POST":
            head_form = ResumeHeadForm(request.POST, request.FILES)
            education_form = ResumeEducationForm(request.POST)
            experience_form = ResumeExperienceForm(request.POST)
            skill_form = ResumeSkillForm(request.POST)
            if head_form.is_valid() and education_form.is_valid() and experience_form.is_valid() and skill_form.is_valid():
                head = head_form.save(commit=False)
                head.user = request.user
                head.save()
                education = education_form.save(commit=False)
                education.resume = head
                education.save()
                experience = experience_form.save(commit=False)
                experience.resume = head
                experience.save()
                skill = skill_form.save(commit=False)
                skill.resume = head
                skill.save()
                messages.success(request,"Resume created successfully")
                return redirect('resume', username=request.user.username)
        else:
            head_form = ResumeHeadForm()
            education_form = ResumeEducationForm()
            experience_form = ResumeExperienceForm()
            skill_form = ResumeSkillForm()
    context = {
        "head_form": head_form,
        "education_form": education_form,
        "experience_form": experience_form,
        "skill_form": skill_form
    }
    return render(request, 'resume/create_new.html', context=context)

def update_resume(request):
    cv = ResumeHead.objects.get(user=request.user)
    if request.method == "POST":
        head_form = ResumeHeadForm(request.POST, request.FILES, instance=cv)
        if head_form.is_valid():
            head_form.save()
            messages.success(request,"Resume updated successfully")
            return redirect('resume', username=request.user.username)
    else:
        head_form = ResumeHeadForm(instance=cv)
    context = {
        "head_form": head_form
    }
    return render(request, 'resume/update_resume.html', context=context)

def delete_resume(request):
    cv = ResumeHead.objects.get(user=request.user)
    if cv.image:
        img_path = os.path.join(settings.MEDIA_ROOT, str(cv.image))
        if os.path.exists(img_path):
            os.remove(img_path)
    cv.delete()
    messages.success(request,"Resume deleted successfully")
    return redirect('create_resume')


def add_education(request):
    if request.method == "POST":
        form = ResumeEducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.resume = ResumeHead.objects.get(user=request.user)
            education.save()
            return redirect('resume', username=request.user.username)
    else:
        form = ResumeEducationForm()
    context = {
        "form": form
    }
    return render(request, 'resume/add.html', context=context)

def add_experience(request):
    if request.method == "POST":
        form = ResumeExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.resume = ResumeHead.objects.get(user=request.user)
            experience.save()
            return redirect('resume',  username=request.user.username)
    else:
        form = ResumeExperienceForm()
    context = {
        "form": form
    }
    return render(request, 'resume/add.html', context=context)

def add_skill(request):
    if request.method == "POST":
        form = ResumeSkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.resume = ResumeHead.objects.get(user=request.user)
            skill.save()
            return redirect('resume', username=request.user.username)
    else:
        form = ResumeSkillForm()
    context = {
        "form": form
    }
    return render(request, 'resume/add.html', context=context)

def delete_education(request, pk):
    education = ResumeEducation.objects.get(pk=pk)
    education.delete()
    return redirect('resume', username=request.user.username)

def delete_experience(request, pk):
    experience = ResumeExperience.objects.get(pk=pk)
    experience.delete()
    return redirect('resume', username=request.user.username)

def delete_skill(request, pk):
    skill = ResumeSkill.objects.get(pk=pk)
    skill.delete()
    return redirect('resume', username=request.user.username)


# ================================ Geocode API ==========================

from .geocode import GeoCode
geocode = GeoCode()
def location(request):
    context = {}
    if request.method == "POST":
        form = LocationForm(request.POST)
        context["form"] = form
        if form.is_valid():
            city = request.POST.get("city")
            res_dict = geocode.forward(city)
            context["city"] = res_dict["location"]
            context["lat"] = res_dict["lat"]
            context["lon"] = res_dict["lon"]
    else:
        form = LocationForm()
        context["form"] = form
    return render(request,"resume/location.html", context=context)

def location_reverse(request):
    context = {}
    if request.method == "POST":
        form = LocationReverseForm(request.POST)
        context["form"] = form
        if form.is_valid():
            lat = request.POST.get("lat")
            lon = request.POST.get("lon")
            res_location = geocode.reverse(lat, lon)
            try:
                context["location"] = res_location
            except Exception as e:
                context["location"] = "Invalid coordinates"
                print(e)
    else:
        form = LocationReverseForm()
        context["form"] = form
    return render(request,"resume/location_reverse.html", context=context)
