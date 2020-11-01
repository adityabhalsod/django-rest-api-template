from base.exceptions import get_status
from rest_framework import status


def response_modification(response):
    """
    Modify API response format.
    """
    if (
        status.is_client_error(response.status_code)
        or status.is_server_error(response.status_code)
    ) and (status.HTTP_400_BAD_REQUEST != response.status_code):
        return response

    # Modify the response data
    modified_data = {}
    modified_data["code"] = response.status_code
    modified_data["status"] = get_status(response.status_code)
    modified_data["data"] = response.data

    response.data = modified_data
    return response


def set_response(message, status=True, http_code=200, result=None):
    response = {}
    response["status"] = status
    response["http_code"] = http_code
    response["message"] = message
    response["result"] = result
    return response
