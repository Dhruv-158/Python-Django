

from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class AdminSuperuserCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated:
                return redirect('login')  # Redirect to login if not logged in
            elif not request.user.is_superuser:
                return HttpResponseForbidden("You do not have permission to access this page.")  # Forbidden if not superuser
        return self.get_response(request)
