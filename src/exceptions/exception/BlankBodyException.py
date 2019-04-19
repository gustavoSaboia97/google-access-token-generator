from .GenericAPIException import GenericAPIException


class BlankBodyException(GenericAPIException):
    def __init__(self):
        super(BlankBodyException, self).__init__(f"Body cannot be blank", 400)
