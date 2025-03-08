from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from uuid import uuid4
import random
from django.conf import settings
from django.core.mail import send_mail
from open_ai_app.views import open_ai
from .forms import *

# Create your views here.
def home(request):

    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if User.objects.filter(username=name).exists():
            user = auth.authenticate(username=name, password=password)
            print(type(name), type(user.username), type(user.email))
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid credentials.")
        elif User.objects.filter(email=name).exists():
            username = User.objects.get(email=name).username
            user = auth.authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid credentials.")
        else:
            messages.warning(request, "User not found.")
            return redirect('register')
        # if user:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     messages.warning(request, "Invalid credentials.")
    return render(request, 'auth/login.html')

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.warning(request, "Username already exists.")
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.set_password(password)
                user.save()
                otp = random.randint(1000, 9999)
                profile = Profile(user=user, token=otp)
                profile.save()
                subject = "Account varification OTP"
                message = f"Your OTP is {otp}"
                from_email = settings.EMAIL_HOST_USER
                recipent = [email]
                send_mail(subject, message, from_email, recipent)

                messages.success(request, "Your  OTP was sent to your email.")
            return redirect('otp')
        else:
            messages.warning(request, "Password didn't match.")

    return render(request, 'auth/register.html')

def otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        try:
            prof= Profile.objects.get(token=otp)
            prof.is_verified = True
            prof.save()
            messages.success(request, "Your Profile Created and verified successfully.")
            return redirect('login')
        except:
            messages.warning(request, "Wrong OTP.")
            return redirect("otp")
    return render(request, 'auth/otp.html')

def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, 'about.html')


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            token =str(uuid4())
            pass_recover = PasswordReset(user=user, token_pass=token)
            pass_recover.save()
            subject = "Password Reset Link"
            message = f"Your user name : {user.username} || Click on the link to reset your password -- http://127.0.0.1:8000/new_pass/{token}/"
            from_email = settings.EMAIL_HOST_USER
            recipent = [email]
            send_mail(subject, message, from_email, recipent)
            messages.success(request, "Password reset link was sent to your email.")
            return redirect('login')
        else:
            messages.warning(request, "Email not found.")
    
    return render(request, 'auth/password_reset.html')

def new_pass(request, token):
    context = {}
    try:
        reset_pass = PasswordReset.objects.get(token_pass=token)
        context = {'user_id': reset_pass.user.id}
        if request.method == "POST":
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            user_id = request.POST.get('user_id')
            if user_id is None:
                messages.warning(request, "User not found.")
                return redirect(f'new_pass/{token}/')
            if password != password1:
                messages.warning(request, "Password didn't match.")
                return redirect(f'new_pass/{token}/')
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(password)
            user_obj.save()
            del_reset = PasswordReset.objects.get(token_pass=token)
            del_reset.delete()
            messages.success(request, "Password reset successfully.")
            return redirect('login')
    except Exception as e:
        messages.warning(request, f"Error: {e}")
        return redirect('login')
    return render(request, 'auth/new_pass.html', context)


def contact(request):
    if request.user.is_active:
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                name = request.POST.get('name')
                message = request.POST.get('message')
                subject = f"Message from {name}"
                message = f"name : {name} \nmessage : {message}"
                from_email = settings.EMAIL_HOST_USER
                recipent = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email, recipent)
                messages.success(request, "Your message was sent successfully.")
                return redirect('contact')

        else:
            form = ContactForm()
    else:
        messages.warning(request, "Please login to continue.")
        return redirect('login')

    return render(request, 'contact.html', {'form': form})