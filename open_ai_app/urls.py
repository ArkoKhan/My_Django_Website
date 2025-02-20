from django.urls import path
from .views import *

urlpatterns = [
    path('open_ai/', open_ai, name='open_ai'),
]