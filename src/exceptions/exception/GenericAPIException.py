class GenericAPIException(Exception):
    def __init__(self, msg: str, status_code: int):
        Exception.__init__(self)
        self.status_code = status_code
        self.message = msg

    def to_dict(self):
        return {
            "message": self.message,
            "status_code": self.status_code
        }
