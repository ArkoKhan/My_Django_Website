from django.urls import path
from .views import *

urlpatterns = [
    path("resume/<str:username>/", resume, name="resume"),
    path("create_resume/", create_resume, name="create_resume"),
    path("update_resume/", update_resume, name="update_resume"),
    path("delete_resume/", delete_resume, name="delete_resume"),
    path("add_education/", add_education, name="add_education"),
    path("add_experience/", add_experience, name="add_experience"),
    path("add_skill/", add_skill, name="add_skill"),
    path("delete_education/<int:pk>/", delete_education, name="delete_education"),
    path("delete_experience/<int:pk>/", delete_experience, name="delete_experience"),
    path("delete_skill/<int:pk>/", delete_skill, name="delete_skill"),
    path("download_resume/<str:username>/", download_resume, name="download_resume"),
    path("generate_pdf/<str:username>/", GeneratePDF.as_view(), name="generate_pdf"),
    path("location/", location, name="location"),
]