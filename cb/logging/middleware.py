import logging


class RequestFilter(logging.Filter):
    def __init__(self, request):
        super().__init__()
        self.request = request

    def filter(self, record):
        if self.request.user.is_authenticated:
            record.username = self.request.user.username
        else:
            record.username = 'AnonymousUser'

        return True


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger = logging.getLogger('cb')
        if not any(isinstance(f, RequestFilter) for f in logger.filters):
            logger.addFilter(RequestFilter(request))

        response = self.get_response(request)
        return response
