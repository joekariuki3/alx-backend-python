from datetime import datetime

class RequestLoggingMiddleware:
    """
    Middleware that logs each user’s requests to a file, including the timestamp, user and the request path
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        log_file = 'requests.log'
        log_string = f"{datetime.now()} - User: {request.user} - Path: {request.path}\n"
        with open(log_file, 'a') as f:
            written_char = f.write(log_string)
        response = self.get_response(request)
        return response