class StudentSystemError(Exception):
    """Base exception for the application."""


class ValidationError(StudentSystemError):
    pass


class NotFoundError(StudentSystemError):
    pass


class DuplicateError(StudentSystemError):
    pass


class AuthenticationError(StudentSystemError):
    pass


class AuthorizationError(StudentSystemError):
    pass


class StorageError(StudentSystemError):
    pass
