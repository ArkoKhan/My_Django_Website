from django.urls import path
from .views import *

urlpatterns = [
path('project_home/', project_home, name='project_home'),
    path('linkedin_job_search/', linkedin_job_search, name='linkedin_job_search'),
]