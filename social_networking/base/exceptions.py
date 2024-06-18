from rest_framework.exceptions import APIException


class BaseAPIException(APIException):
    pass


class TooManyRequestsException(APIException):
    pass
