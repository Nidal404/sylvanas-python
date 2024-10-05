from typing import Optional, Dict, List

from sylvanas.Enums import ExceptionLevel


class SylvanasBaseException(Exception):
    """ Project base exception"""


class ApplicationException(SylvanasBaseException):

    def __init__(self, message: str, level: ExceptionLevel = ExceptionLevel.ERROR):
        self.message: str = message
        self.level: ExceptionLevel = level


class ArgumentException(SylvanasBaseException):  # JsonSchema validation

    def __init__(self, errors: List):
        self.errors: List = errors


class DevException(SylvanasBaseException):  # Message pour moi même si je sais pas use une class

    def __init__(self, message: str):
        self.message: str = message


"""
Exceptions liées aux clients
"""


class ClientException(SylvanasBaseException):
    """Exception à traiter coté client"""

    def __init__(self, code: int, message: str, data: Optional[Dict] = None):
        self.code: int = code
        self.message: str = message
        self.data: Optional[Dict] = data


class ApiAuthError(SylvanasBaseException):
    """Erreur gérée côté client pour le basic ou le bearer"""
