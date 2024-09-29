import re
from abc import ABC
from typing import Optional


class ValidationUtils(ABC):

    @staticmethod
    def isEmailValid(email: str) -> bool:
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(email_regex, email))

    @staticmethod
    def isStrNullOrEmpty(value: Optional[str]) -> bool:
        if value is None:
            return True

        if not isinstance(value, str):
            raise TypeError('Value must be a str')

        return not value.strip()