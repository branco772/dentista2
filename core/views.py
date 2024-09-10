from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def especialidad(request):
    return render(request, 'core/especialidad.html')

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data={
        'form': CustomUserCreationForm()
    }
    return render(request, 'registration/register.html', data)