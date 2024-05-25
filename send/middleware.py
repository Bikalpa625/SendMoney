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
        # List of URLs that don't require authentication
        allowed_urls = [
            reverse('login'),
            reverse('register'),
            reverse('password_reset'),
            reverse('password_reset_done'),
            reverse('password_reset_confirm', kwargs={'uidb64': 'uidb64', 'token': 'token'}),
            reverse('password_reset_complete'),
        ]

        if request.path in allowed_urls:
            return None

        if not request.user.is_authenticated:
            messages.warning(request, "You need to be logged in to access this page.")
            return redirect('login')

        return None
