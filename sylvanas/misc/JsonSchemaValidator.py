from typing import Union, Dict, List

from jsonschema.exceptions import ValidationError
from jsonschema.validators import Draft7Validator

from sylvanas.Enums import ExceptionLevel
from sylvanas.Exceptions import ArgumentException, ApplicationException
from sylvanas.utils.ValidationUtils import ValidationUtils


class JsonSchemaValidator:
    def __init__(self, schema: Dict, json: Union[Dict, List]):
        if not isinstance(json, dict) and not isinstance(json, list):
            raise ArgumentException(['JSON can\'t be empty'])

        if not isinstance(schema, dict):
            raise ApplicationException("Schema is not valid", ExceptionLevel.ERROR)

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

        if 'id' in self.json and not ValidationUtils.isGuidValid(self.json['id']):
            errors.append(ValidationError(f'Id {self.json['id']}, is not a valid Guid'))

        return [error.message for error in errors]
