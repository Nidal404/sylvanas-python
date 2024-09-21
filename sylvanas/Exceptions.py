from typing import Optional, Dict

from sylvanas.Enums import ExceptionLevel


class SylvanasBaseException(Exception):
    """ Project base exception"""


class ApplicationException(SylvanasBaseException):

    def __init__(self, message: str, level: ExceptionLevel):
        self.message: str = message
        self.level: ExceptionLevel = level


class ArgumentException(SylvanasBaseException):

    def __init__(self, message: str):
        self.message: str = message


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
