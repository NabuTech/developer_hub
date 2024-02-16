# accounts/urls.py
from django.urls import path
from .views import signup_view

urlpatterns = [
    # Other URL patterns...
    path('signup/', signup_view, name='signup'),
]
