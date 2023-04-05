import os
from pathlib import Path
import json
import jsonschema
from jsonschema import validate
from abc import ABC, abstractmethod, ABCMeta


class Base(ABC):
    BASIC_URL = "https://product-api.services.preprod.wickes.systems/product/v1"

    @staticmethod
    def construct_url(api, common_url=BASIC_URL):
        return common_url + api

    @staticmethod
    def root_dir(file_dir):
        ROOT_DIR = os.path.dirname(os.path.abspath(file_dir.__file__))
        return ROOT_DIR

    def file_data(self, path):
        txt = Path(path).read_text()
        return txt

    @staticmethod
    def validateJson(response, jsonSchema):
        try:
            jsonDataDictionary = json.dumps(response)
            jsonDataString = json.loads(jsonDataDictionary)
            validate(instance=jsonDataString, schema=jsonSchema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True