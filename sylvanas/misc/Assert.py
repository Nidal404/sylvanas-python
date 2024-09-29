import uuid
from abc import ABC
from datetime import datetime
from typing import Any, Callable, Dict

from sylvanas.Exceptions import DevException


class Assert(ABC):
    @staticmethod
    def isTrue(condition: bool):
        assert condition, "\nTrue Expected"

    @staticmethod
    def isFalse(condition: bool):
        assert not condition, "\nFalse Expected"

    @staticmethod
    def isTimestamp(value):
        try:
            dt = datetime.fromtimestamp(value)
            if dt.year <= 1970:  # Ensure it's a timestamp from the epoch
                raise AssertionError(f"Timestamp must be after January 1, 1970, got {value}")
        except Exception:
            raise AssertionError(f"Expected timestamp, got {str(value)}")

    @staticmethod
    def isMoreThan(expected, actual):
        assert actual > expected, f"\nExpected: {expected} to be more then {actual}"

    @staticmethod
    def areEqual(expected: Any, actual: Any):
        assert expected == actual, f"\nExpected: {expected}\nActual: {actual}"

    @staticmethod
    def areNotEqual(unexpected: Any, actual: Any):
        assert unexpected != actual, f"\nUnexpected: {unexpected}\nActual: {actual}"

    @staticmethod
    def isNone(value: Any):
        assert value is None, f"\nExpected None, but got: {value}"

    @staticmethod
    def isNotNone(value: Any):
        assert value is not None, f"\nExpected non-None value, but got None"

    @staticmethod
    def isGuid(value):
        try:
            uuid.UUID(str(value))  # Attempt to create a UUID from the value
        except Exception:
            raise AssertionError(f"Expected Guid, got {str(value)}")

    @staticmethod
    def mustContains(expectedStr: str, value: str):
        if expectedStr and expectedStr not in value:
            raise AssertionError(f"Expected '{expectedStr}' in {value}")

    @staticmethod
    def hasRaise(exception: type, func: Callable, *args, msg: str = "", **kwargs):
        try:
            func(*args, **kwargs)
            raise AssertionError(f"Expected {exception.__name__} to be raised, but no exception was raised")
        except exception as ex:
            if msg and msg not in str(ex):
                raise AssertionError(f"Expected exception message '{msg}', but got '{str(ex)}'")
        except Exception as e:
            raise AssertionError(f"Expected {exception.__name__} to be raised, but {type(e).__name__} was raised")

    @staticmethod
    def areEntityPropertyCountEqual(expectedEntityPropertyCount: int, obj):
        propertyCount = len(vars(obj)) - 1
        if propertyCount != expectedEntityPropertyCount:
            raise AssertionError(f"Expected porperties count from {obj.__class__.__name__} to be {expectedEntityPropertyCount}, go {propertyCount}")

    @staticmethod
    def areEntityPropertiesEqual(obj, data: Dict):
        if not isinstance(data, dict) and len(data) == 0:
            raise DevException('Data has to be a non empty dictionnary')

        for key, value in data.items():
            if not hasattr(obj, key):
                raise AttributeError(f"Object has no attribute '{key}'")

        Assert.isGuid(getattr(obj, 'id'))
        Assert.isTimestamp(getattr(obj, 'created_datetime'))

        for key, value in data.items():
            objProperty = getattr(obj, key)

            if callable(value):
                if not value(objProperty):
                    raise AssertionError(f"Property '{key}' does not match: Expected {value}")
            elif objProperty != value:
                raise AssertionError(f"Property '{key}' does not match: Expected {value}, got {objProperty}")
