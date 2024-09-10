from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
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
    if request.method=='POST':
        userCreationForm=CustomUserCreationForm(data=request.POST)
        if userCreationForm.is_valid():
            userCreationForm.save()
            user=authenticate(username=userCreationForm.cleaned_data['username'], password=userCreationForm.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html', data)