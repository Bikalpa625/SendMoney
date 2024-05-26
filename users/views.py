from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)
    
@login_required
def register(request):
    return render(request, 'users/register.html')


@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')

