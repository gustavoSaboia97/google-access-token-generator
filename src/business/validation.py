from src.exceptions.exceptions import CannotBeBlankException, BlankBodyException
from src.util.logger import get_logger

log = get_logger()


def validate_to_refresh_token(app_data):
    if app_data is None:
        raise BlankBodyException()
    if "client_id" not in app_data:
        raise CannotBeBlankException("client_id")
    if "client_secret" not in app_data:
        raise CannotBeBlankException("client_secret")
    if "code" not in app_data:
        raise CannotBeBlankException("code")
    if "redirect_uri" not in app_data:
        raise CannotBeBlankException("redirect_uri")
    if not bool(app_data["client_id"].strip()):
        raise CannotBeBlankException("client_id")
    if not bool(app_data["client_secret"].strip()):
        raise CannotBeBlankException("client_secret")
    if not bool(app_data["code"].strip()):
        raise CannotBeBlankException("code")
    if not bool(app_data["redirect_uri"].strip()):
        raise CannotBeBlankException("redirect_uri")


def validate_to_access_token(app_data):
    if app_data is None:
        raise BlankBodyException()
    if "client_id" not in app_data:
        raise CannotBeBlankException("client_id")
    if "client_secret" not in app_data:
        raise CannotBeBlankException("client_secret")
    if "refresh_token" not in app_data:
        raise CannotBeBlankException("refresh_token")
    if not bool(app_data["client_id"].strip()):
        raise CannotBeBlankException("client_id")
    if not bool(app_data["client_secret"].strip()):
        raise CannotBeBlankException("client_secret")
    if not bool(app_data["refresh_token"].strip()):
        raise CannotBeBlankException("refresh_token")
