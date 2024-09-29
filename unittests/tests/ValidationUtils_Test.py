from sylvanas.utils.ValidationUtils import ValidationUtils
from sylvanas.misc.Assert import Assert


class TestValidationUtils:

    def test_isEmailValid(self):
        Assert.isTrue(ValidationUtils.isEmailValid('marci@polo.fr'))
        Assert.isFalse(ValidationUtils.isEmailValid('marci@polo'))
        Assert.isFalse(ValidationUtils.isEmailValid('marci'))

    def test_isNullOrEmpty(self):
        Assert.isTrue(ValidationUtils.isStrNullOrEmpty(None))
        Assert.hasRaise(TypeError, ValidationUtils.isStrNullOrEmpty, 5, msg='Value must be a str')
        Assert.isTrue(ValidationUtils.isStrNullOrEmpty(''))
        Assert.isTrue(ValidationUtils.isStrNullOrEmpty('  '))
        Assert.isFalse(ValidationUtils.isStrNullOrEmpty(' c '))
        Assert.isFalse(ValidationUtils.isStrNullOrEmpty('coucou'))
        Assert.isFalse(ValidationUtils.isStrNullOrEmpty('5'))
