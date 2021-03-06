from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username= request.POST['username']
            password= request.POST['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('blog-home')
    else:
        form=RegistrationForm()
    context={'form':form}
    return render(request, 'users/register.html',context)

