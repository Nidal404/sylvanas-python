from abc import ABC


class TextFormatUtils(ABC):

    @staticmethod
    def strToBool(val) -> bool:
        if type(val) is bool:
            return bool(val)
        if type(val) is int:
            return bool(val)

        val = val.lower()
        if val in ('y', 'yes', 't', 'true', 'on', '1', 'True'):
            return True
        elif val in ('n', 'no', 'f', 'false', 'off', '0', 'False'):
            return False
        else:
            raise ValueError("invalid truth value %r" % (val,))
