from jsonschema.exceptions import ValidationError

from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid
from sylvanas.misc.JsonSchemaValidator import JsonSchemaValidator
from sylvanas.utils.RandomUtils import RandomUtils


class TestJsonSchema:
    schema = {
        "type": "object",
        "trim": ["trimable_str"],
        "required": ["id"],
        "properties": {
            "id": {"type": "string", "minLength": 36, "maxLength": 36},
            "trimable_str": {"type": "string", "minLength": 1, "maxLength": 30},
        }
    }

    def test_SchemaValidation(self):
        def AssertTrim():
            body = {
                'id': Guid.new(),
                'trimable_str': ' trimeuxmoi     ',
            }

            JsonSchemaValidator(self.schema, body).validate()
            Assert.areEqual('trimeuxmoi', body['trimable_str'])

        def AssertId():
            results = JsonSchemaValidator(self.schema, {'id': RandomUtils.generateString(size=36)}).validate()
            Assert.areEqual(1, len(results))
            Assert.mustContains('is not a valid Guid', results[0])

        AssertTrim()
        AssertId()
