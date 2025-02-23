from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('about/', about, name='about'),
    path('otp/', otp, name='otp'),
    path("password_reset/", password_reset, name="password_reset"),
    path("new_pass/<token>/", new_pass, name="new_pass"),
    path("contact/", contact, name="contact"),
]