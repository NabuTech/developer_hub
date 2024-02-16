# accounts/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm  # Import your custom form
from django.contrib import messages

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
