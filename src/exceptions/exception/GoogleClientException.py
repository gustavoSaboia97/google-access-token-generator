from .GenericAPIException import GenericAPIException


class GoogleClientException(GenericAPIException):
    def __init__(self, message: str, status_code: int):
        super(GoogleClientException, self).__init__(message, status_code)
