from enum import Enum

from sylvanas.misc.ExtendedEnum import ExtendedIntEnum


class DateFormat(Enum):
    FORMAT_YYYYMMDD = '%Y%m%d'
    FORMAT_YYYYMMDD_WITH_DASH = '%Y-%m-%d'
    FORMAT_YYYYMMDD_hhmmss_WITH_DASH = '%Y-%m-%d %H:%M:%S'
    FORMAT_YYYYMMDD_hhmmssff_WITH_DASH = '%Y-%m-%d %H:%M:%S.%f'
    FORMAT_DDMMYYYY_WITH_SLASH = '%d/%m/%Y'


class ProjectEnvironmentType(Enum):
    DEVELOPMENT = 'dev'
    PRODUCTION = 'prod'
    TEST = 'test'


class TimeInSecond(ExtendedIntEnum):
    ONE_MINUTE = 60
    ONE_HOUR = 3600
    ONE_DAY = 86400


class MobilePlatformType(ExtendedIntEnum):
    APPLE = 2
    GOOGLE = 3


class ExceptionLevel(ExtendedIntEnum):
    INFO = 2
    WARNING = 5
    ERROR = 10
