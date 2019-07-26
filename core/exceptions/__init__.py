from sanic.exceptions import SanicException, add_status_code


@add_status_code(401)
class UnknownFieldException(SanicException):
    def __init__(self):
        message = 'Unknown field inside request'
        super().__init__(message=message)
