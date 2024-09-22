from sylvanas.misc.Assert import Assert
from sylvanas.misc.Guid import Guid
from sylvanas.misc.JsonSchemaValidator import JsonSchemaValidator


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
        body = {
            'id': Guid.new(),
            'trimable_str': ' trimeuxmoi     ',
        }

        results = JsonSchemaValidator(self.schema, body).validate()
        Assert.areEqual('trimeuxmoi', body['trimable_str'])
