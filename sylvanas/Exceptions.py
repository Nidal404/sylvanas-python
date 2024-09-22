from typing import Optional, Dict, List

from sylvanas.Enums import ExceptionLevel


class SylvanasBaseException(Exception):
    """ Project base exception"""


class ApplicationException(SylvanasBaseException):

    def __init__(self, message: str, level: ExceptionLevel):
        self.message: str = message
        self.level: ExceptionLevel = level


class ArgumentException(SylvanasBaseException):  # JsonSchema validation

    def __init__(self, message: str, errors: List):
        self.message: str = message
        self.errors: List = errors


"""
Exceptions liées aux clients
"""


class ApiException(SylvanasBaseException):
    """Exception à traiter coté client"""

    def __init__(self, code: int, message: str, data=None):
        self.code: int = code
        self.message: str = message
        self.data: Optional[Dict] = data


class ApiAuthError(SylvanasBaseException):
    """Erreur gérée côté client pour le basic ou le bearer"""
