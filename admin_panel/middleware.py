from django.shortcuts import render


class BanMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.user.is_authenticated
            and request.user.is_banned
            and request.path != '/logout/'  # Exclude '/logout/' from ban check
        ):
            # User is banned, redirect them or return a response
            return render(request, 'admin_panel/banned_page.html')

        response = self.get_response(request)
        return response
