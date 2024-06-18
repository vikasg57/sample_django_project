from rest_framework import status
from rest_framework.views import exception_handler

from base.exceptions import (
    BaseAPIException,
    TooManyRequestsException
)
from base.response import APIResponse


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    data = {
        'code': '00001',
        'message': 'Unknown Internal Server Error'
    }
    try:
        if exc is not None:
            # TODO Keeping it true to start with, change later.
            data = {
                'code': exc.get_codes(),
                'message': exc.detail
            }
            if isinstance(exc, BaseAPIException):
                status_code = status.HTTP_400_BAD_REQUEST
            elif isinstance(exc, TooManyRequestsException):
                status_code = status.HTTP_429_TOO_MANY_REQUESTS
            else:
                status_code = exc.status_code if (
                    exc.status_code) else status.HTTP_400_BAD_REQUEST
                if status_code is not status.HTTP_403_FORBIDDEN:
                    data = {
                        'code': exc.get_codes().get('code'),
                        'message': exc.detail.get("detail").title()
                    }
                else:
                    data = {
                        'code': exc.get_codes(),
                        'message': exc.detail.title()
                    }
        if response is not None:
            response.data['status_code'] = response.status_code
    except Exception as e:
        print("exception while raising proper exception", e, exc)

    return APIResponse(data=data, status=status_code)
