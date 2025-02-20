from django.shortcuts import render, redirect
from  .gpt import GPT
from .forms import *
from .models import ChatTable
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

gpt = GPT()


# @login_required(login_url='login')
def open_ai(request):
    if request.user.is_active:
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():
                msg = request.POST.get('prompt')
                if not ChatTable.objects.filter(prompt=msg).exists():
                    output = gpt.chat(msg)
                    chat = ChatTable(prompt=msg, output=output)
                    chat.save()
                else:
                    chat = ChatTable.objects.get(prompt=msg)
                    output = chat.output
                context = {'msg': output, 'form': form}
                return render(request, 'open_ai/gpt.html', context)
        else:
            form = InputForm()
    else:
        messages.warning(request, "Please login to continue.")
        return redirect('login')

    return render(request, 'open_ai/gpt.html', {'form': form})