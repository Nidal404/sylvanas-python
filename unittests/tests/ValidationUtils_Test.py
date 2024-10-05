import uuid

from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid
from sylvanas.utils.RandomUtils import RandomUtils
from sylvanas.utils.ValidationUtils import ValidationUtils


class TestValidationUtils:

    def test_isGuidValid(self):
        Assert.isFalse(ValidationUtils.isGuidValid(None))
        Assert.isFalse(ValidationUtils.isGuidValid(''))
        Assert.isFalse(ValidationUtils.isGuidValid(RandomUtils.generateString(size=32)))
        Assert.isFalse(ValidationUtils.isGuidValid(RandomUtils.generateString(size=36)))
        Assert.isFalse(ValidationUtils.isGuidValid(uuid.UUID(int=0)))
        Assert.isTrue(ValidationUtils.isGuidValid(Guid.new()))

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
