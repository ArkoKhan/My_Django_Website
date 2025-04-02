from django.shortcuts import render, redirect
from .forms import JobSearchForm
from .linked_in_job import LinkedInJobSearch

# Create your views here.

def project_home(request):
    return render(request, 'api/project_home.html')


def linkedin_job_search(request):
    job_search = LinkedInJobSearch()
    context = {}
    if request.method == "POST":
        form = JobSearchForm(request.POST)
        context['form'] = form
        if form.is_valid():
            job_title = request.POST.get('job_title')
            location = request.POST.get('location')
            remote_filter = request.POST.get('remote_filter')
            jobs = job_search.search_jobs(job_title, location, remote_filter)
            context['jobs'] = jobs
    else:
        form = JobSearchForm()
        context['form'] = form

    return render(request, 'api/linkedin_job_search.html', context)