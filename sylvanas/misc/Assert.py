from abc import ABC
from typing import Any, Callable


class Assert(ABC):
    @staticmethod
    def isTrue(condition: bool):
        assert condition, "\nTrue Expected"

    @staticmethod
    def isFalse(condition: bool):
        assert not condition, "\nFalse Expected"

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
    def hasRaise(exception: type, func: Callable, *args, msg: str = "", **kwargs):
        try:
            func(*args, **kwargs)
            raise AssertionError(f"Expected {exception.__name__} to be raised, but no exception was raised")
        except exception as ex:
            if msg and msg not in str(ex):
                raise AssertionError(f"Expected exception message '{msg}', but got '{str(ex)}'")
        except Exception as e:
            raise AssertionError(f"Expected {exception.__name__} to be raised, but {type(e).__name__} was raised")
