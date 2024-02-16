# core/urls.py
from django.urls import path
from .views import home, login_page, signup_view, dashboard, userprofile, projects, collaboration, network, about

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('projects/', projects, name='projects'),
    path('userprofile/', userprofile, name='userprofile'),
    path('collaboration/', collaboration, name='collaboration'),
    path('network/', network, name='network'),
    path('about/', about, name='about'),
]
