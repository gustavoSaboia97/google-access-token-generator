from flask import Blueprint, request, Response

from src.components.url_components import API_REFRESH_TOKEN_GENERATOR, API_ACCESS_TOKEN_GENERATOR
from src.controllers.GoogleController import GoogleController
from src.exceptions.ExceptionHandler import ExceptionHandler
from src.exceptions.exceptions import GenericAPIException

google_blueprint = Blueprint("google_blueprint", __name__)

google_controller = GoogleController()
exception_handler = ExceptionHandler()


@google_blueprint.route(API_REFRESH_TOKEN_GENERATOR, methods=['POST', ])
def refresh_token_and_access_token_generator() -> Response:
    app_data = request.json
    return google_controller.generate_refresh_token_and_access_token(app_data)


@google_blueprint.route(API_ACCESS_TOKEN_GENERATOR, methods=['POST', ])
def access_token_generator() -> Response:
    app_data = request.json
    return google_controller.generate_access_token(app_data)


@google_blueprint.errorhandler(GenericAPIException)
def api_error_handler(exception: GenericAPIException) -> Response:
    return exception_handler.api_exception(exception)


@google_blueprint.errorhandler(Exception)
def generic_error_handler(exception: Exception) -> Response:
    return exception_handler.generic_exception(exception)
