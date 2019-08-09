from sanic.exceptions import SanicException, add_status_code


@add_status_code(401)
class UnknownFieldException(SanicException):
    def __init__(self):
        message = 'Unknown field inside request'
        super().__init__(message=message)


@add_status_code(400)
class ValidationErrorException(SanicException):
    def __init__(self):
        message = 'Validation error'
        super().__init__(message)


@add_status_code(401)
class PermissionErrorException(SanicException):
    def __init__(self):
        message = 'Permission error'
        super().__init__(message)


@add_status_code(401)
class InvalidJoinTypeException(SanicException):
    def __init__(self):
        message = 'Invalid join type'
        super().__init__(message=message)


@add_status_code(401)
class SocialLoginFailException(SanicException):
    def __init__(self):
        message = 'Social login fail'
        super().__init__(message=message)


@add_status_code(401)
class NotUniqueException(SanicException):
    def __init__(self):
        message = 'Not unique'
        super().__init__(message=message)


@add_status_code(401)
class UnknownException(SanicException):
    def __init__(self):
        message = 'Unknown'
        super().__init__(message=message)


@add_status_code(401)
class DuplicateException(SanicException):
    def __init__(self):
        message = 'Duplicate error'
        super().__init__(message=message)
