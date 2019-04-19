from src.business.validation import validate_to_refresh_token, validate_to_access_token
from src.client.GoogleClient import GoogleClient
from src.util.logger import get_logger

log = get_logger()


class GoogleBusiness:

    def __init__(self):
        self.__client = GoogleClient()

    def generate_refresh_token_and_access_token(self, app_data: dict) -> dict:
        log.info(f"[GOOGLE BUSINESS - REFRESH TOKEN] Validating necessary data with json {app_data}")
        validate_to_refresh_token(app_data)
        json_repose = self.__client.request_refresh_token_and_access_token(app_data)
        return json_repose

    def generate_access_token(self, app_data: dict) -> dict:
        log.info(f"[GOOGLE BUSINESS - ACCCESS TOKEN] Validating necessary data with json {app_data}")
        validate_to_access_token(app_data)
        json_repose = self.__client.request_access_token(app_data)
        return json_repose
