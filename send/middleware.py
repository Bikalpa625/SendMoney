from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to access certain pages.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Skip login, register and admin URLs
        if not request.user.is_authenticated and request.path not in [reverse('login'), reverse('register'), reverse('admin:index')]:
            messages.warning(request, "You need to log in to access this page.")
            return redirect('login')
        return None
