from abc import ABC
from datetime import datetime, timezone


class DateUtils(ABC):

    @staticmethod
    def UtcNow():
        return datetime.now(timezone.utc).timestamp()
