import logging
import traceback

from django.http import JsonResponse

from base.helper import set_response


class ExceptionMiddleware(object):
    def __init__(self, set_response):
        self.set_response = set_response

    def __call__(self, request):
        response = self.set_response(request)
        response["Access-Control-Allow-Origin"] = "*" # Allow-origin for access control in headers

        if response.status_code == 500:
            response = set_response(
                "Internal server error",
                False,
                500,
                {},
            )
            return JsonResponse(response, status=response["http_code"])

        if response.status_code == 404 and "<h1>Not Found</h1>" in str(
            response.content
        ):
            logging.error(response.content)
            response = set_response("Page not found", False, response.status_code, {})
            return JsonResponse(response, status=response["http_code"])
        return response

    def process_exception(self, request, exception):
        """
        All logging of internal server error HTTP 500
        """
        logging.error("ERROR")
        logging.error(traceback.format_exc())
        response = set_response("Internal server error", False, 500, {})
        return JsonResponse(response, status=response["http_code"])
