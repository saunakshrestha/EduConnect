from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

import logging

from account.forms import EduConnectAuthenticationForm

logger = logging.getLogger('educonnect_logger')

def login_view(request):
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    if request.method == 'POST':
        form = EduConnectAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"User {user} logged in")
            return redirect('home')
    else:
        form = EduConnectAuthenticationForm()
    logger.info(form.errors)
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('account:login')  # Redirect to login page after logout
