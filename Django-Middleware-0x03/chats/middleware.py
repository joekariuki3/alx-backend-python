from datetime import datetime, time, timedelta
from django.http.response import HttpResponseForbidden
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import UserRole


class RequestLoggingMiddleware:
    """
    Middleware that logs each user’s requests to a file, including the timestamp, user and the request path
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before getting to view, request before getting to the view

        log_file = 'requests.log'
        log_string = f"{datetime.now()} - User: {request.user} - Path: {request.path}\n"
        with open(log_file, 'a') as f:
            written_char = f.write(log_string)

        response = self.get_response(request)

        # After the view, response back to a client

        return response

class RestrictAccessByTimeMiddleware:
    """
    middleware that restricts access to the messaging up during certain hours of the day.
    check the current server time and deny access by returning an error 403 Forbidden.
    if a user accesses the chat outside 9PM and 6PM.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()
        restrict_start_time = time(21,00) # 9PM
        restrict_end_time = time(18, 00) # 6PM
        if restrict_start_time <= current_time <= restrict_end_time:
            return HttpResponseForbidden("Access to messaging restricted")

        response = self.get_response(request)
        return response

class OffensiveLanguageMiddleware:
    """
    Middleware that limits the number of chat messages a user can send within a certain time window,
    based on their IP address.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_per_ip = {}
        self.time_window = 60  # 1 minute
        self.max_post_requests = 10  # 10 messages per minute

    def __call__(self, request):
        """
        Count the number of POST requests (messages) from each IP address and implement
        a time window during which a user can only send a limited number of messages.
        """
        if request.method == 'POST':
            ip_address = request.META.get('REMOTE_ADDR')
            current_time = datetime.now()

            # Clean up old entries
            self._cleanup_old_requests(current_time)

            if ip_address not in self.requests_per_ip:
                self.requests_per_ip[ip_address] = []

            # Add current request timestamp
            self.requests_per_ip[ip_address].append(current_time)

            # Count requests within the time window
            window_start = current_time - timedelta(seconds=self.time_window)
            requests_in_window = sum(
                1 for timestamp in self.requests_per_ip[ip_address]
                if timestamp > window_start
            )

            if requests_in_window > self.max_post_requests:
                return HttpResponseForbidden(
                    f"Rate limit exceeded. Maximum {self.max_post_requests} messages per {self.time_window} seconds."
                )

        response = self.get_response(request)
        return response

    def _cleanup_old_requests(self, current_time):
        """Remove entries older than the time window"""
        window_start = current_time - timedelta(seconds=self.time_window)
        for ip in list(self.requests_per_ip.keys()):
            self.requests_per_ip[ip] = [
                timestamp for timestamp in self.requests_per_ip[ip]
                if timestamp > window_start
            ]
            if not self.requests_per_ip[ip]:
                del self.requests_per_ip[ip]

class RolepermissionMiddleware:
    """
    Middleware that checks a user role before allowing access to specific actions.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authentication = JWTAuthentication()

    def __call__(self, request):
        try:
            user_auth_tuple = self.jwt_authentication.authenticate(request)
            if user_auth_tuple is not None:
                user, token = user_auth_tuple
                request.user = user
                if request.user.role not in [UserRole.ADMIN, UserRole.MODERATOR]:
                    message = (f"Access to messaging restricted. You are `{request.user.role}`."
                               f"only `{UserRole.ADMIN}` and `{UserRole.MODERATOR}` has access.")
                    return HttpResponseForbidden(message)
        except AuthenticationFailed:
            pass # view will handle unauthenticated access
        response = self.get_response(request)
        return response