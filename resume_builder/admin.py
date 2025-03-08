from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ResumeHead)
admin.site.register(ResumeEducation)
admin.site.register(ResumeExperience)
admin.site.register(ResumeSkill)