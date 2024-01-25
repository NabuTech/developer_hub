from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render (request, 'login.html')

def signup(request):
    return render (request, 'signup.html')

def dashboard(request):
    return render (request, 'dashboard.html')

def userprofile(request):
    return render (request, 'userprofile.html')

def projects(request):
    return render (request, 'projects.html')

def collaboration(request):
    return render (request, 'collaboration.html' )

def network (request):
    return render (request, 'network.html')

def about (request):
    return render (request, 'about.html')

