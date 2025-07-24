from datetime import datetime, time
from django.http.response import HttpResponseForbidden


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