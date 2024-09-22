from sylvanas.Utils.ValidationUtils import ValidationUtils
from sylvanas.misc.Assert import Assert


class TestValidationUtils:

    def test_Validation(self):
        Assert.isTrue(ValidationUtils.isEmailValid('marci@polo.fr'))
        Assert.isFalse(ValidationUtils.isEmailValid('marci@polo'))
        Assert.isFalse(ValidationUtils.isEmailValid('marci'))