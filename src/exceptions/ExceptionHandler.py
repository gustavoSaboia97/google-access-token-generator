from json import dumps

from flask import Response

from src.exceptions.exception import GenericAPIException
from src.util.logger import get_logger

log = get_logger()


class ExceptionHandler:

    def api_exception(self, exception: GenericAPIException):
        log.error(f"[API ERROR] Error during request process {exception.message}")
        error_json = dumps(exception.to_dict())
        return Response(error_json, status=exception.status_code)

    def generic_exception(self, exception: Exception):
        log.error(f"[API ERROR] Error during request process {str(exception)}")
        return Response(str(exception), status=500)
