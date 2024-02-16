# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm  # Import your custom form
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    # Basic implementation, replace with your actual dashboard logic
    return render(request, 'dashboard.html')

def userprofile(request):
    return render(request, 'userprofile.html')

def projects(request):
    return render(request, 'projects.html')

def collaboration(request):
    return render(request, 'collaboration.html')

def network(request):
    return render(request, 'network.html')

def about(request):
    return render(request, 'about.html')
