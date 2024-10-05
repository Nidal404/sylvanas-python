import re
import uuid
from abc import ABC
from typing import Optional


class ValidationUtils(ABC):

    @staticmethod
    def isGuidValid(value):
        try:
            guid = uuid.UUID(str(value))
            return guid != uuid.UUID(int=0)  # Ensure it is not an empty GUID
        except ValueError:
            return False

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
