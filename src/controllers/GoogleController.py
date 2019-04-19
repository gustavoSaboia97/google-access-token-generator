from json import dumps

from flask import Response

from src.business.GoogleBusiness import GoogleBusiness
from src.components.header_components import JSON_RESPONSE_HEADER
from src.util.logger import get_logger

log = get_logger()


class GoogleController:

    def __init__(self):
        self.__google_business = GoogleBusiness()

    def generate_refresh_token_and_access_token(self, app_data: dict) -> Response:
        log.info(f"[GOOGLE CONTROLLER] Generation of refresh token and access token with data: {app_data}")
        json_response = self.__google_business.generate_refresh_token_and_access_token(app_data)
        serialized_json_reponse = dumps(json_response)
        return Response(serialized_json_reponse, status=200, headers=JSON_RESPONSE_HEADER)

    def generate_access_token(self, app_data: dict) -> Response:
        log.info(f"[GOOGLE CONTROLLER] Generation of access token with data: {app_data}")
        json_response = self.__google_business.generate_access_token(app_data)
        serialized_json_reponse = dumps(json_response)
        return Response(serialized_json_reponse, status=200, headers=JSON_RESPONSE_HEADER)
