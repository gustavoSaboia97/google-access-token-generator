from src.components.google_components import GOOGLE_TOKEN_ENDPOINT, GOOGLE_TOKEN_ENDPOINT_QUERY_STRING
from src.util.logger import get_logger
from src.exceptions.exceptions import GoogleClientException
import requests

from src.components.header_components import GOOGLE_REQUEST_HEADER

log = get_logger()


class GoogleClient:

    def request_refresh_token_and_access_token(self, app_data: dict) -> dict:
        log.info(f"[GOOGLE CLIENT - REFRESH TOKEN] Requesting data to get ACCESS_TOKEN and REFRESH_TOKEN "
                 f"{GOOGLE_TOKEN_ENDPOINT_QUERY_STRING}")
        app_data["grant_type"] = "authorization_code"
        app_data["access_type"] = "offline"
        response = requests.post(GOOGLE_TOKEN_ENDPOINT_QUERY_STRING, headers=GOOGLE_REQUEST_HEADER, data=app_data)

        if response.status_code != 200:
            raise GoogleClientException(response.json(), response.status_code)

        return response.json()

    def request_access_token(self, app_data: dict) -> dict:
        log.info(f"[GOOGLE CLIENT - ACCESS TOKEN] Requesting data to get ACCESS_TOKEN at {GOOGLE_TOKEN_ENDPOINT}")
        app_data["grant_type"] = "authorization_code"
        app_data["access_type"] = "offline"
        response = requests.post(GOOGLE_TOKEN_ENDPOINT, headers=GOOGLE_REQUEST_HEADER, data=app_data)

        if response.status_code != 200:
            raise GoogleClientException(response.json(), response.status_code)

        return response.json()
