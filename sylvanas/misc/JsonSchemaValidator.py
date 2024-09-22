from typing import Union, Dict, List

from jsonschema.validators import Draft7Validator

from sylvanas.Exceptions import ArgumentException, ApplicationException


class JsonSchemaValidator:
    def __init__(self, schema: Dict, json: Union[Dict, List]):
        if not isinstance(json, dict) and not isinstance(json, list):
            raise ArgumentException('Invalid JSON', ['JSON can\'t be empty'])

        if not isinstance(schema, dict):
            raise ApplicationException("Schema is not valid")

        self.schema: Dict = schema
        self.json: Union[Dict, List] = json

        # On rajoute quelques info
        # self.schema['$schema'] = "http://json-schema.org/schema#"
        self.schema['additionalProperties'] = False

    def _trim(self):
        # Trim
        if 'trim' in self.schema:
            for key in self.schema.get('trim', []):
                value = self.json.get(key)
                if isinstance(value, str):
                    self.json[key] = value.strip()

    def validate(self):
        self._trim()

        v = Draft7Validator(self.schema)
        errors = list(v.iter_errors(self.json))  # Liste de ValidationError
        return [error.message for error in errors]
