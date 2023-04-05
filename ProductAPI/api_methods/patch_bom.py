import os

from ProductAPI.base import Base
import json

from ProductAPI.files import PATCH_bom


class PatchBomMethods(Base):
    ACTIVITY_API_WITH_PRODUCT = "/product/320010/bom"
    ACTIVITY_API_WITH_UNEXISTED_PRODUCT = "/product/320000/bom"
    ACTIVITY_API_WITHOUT_PRODUCT = "/product/bom"
    files_dir = PATCH_bom

    def url_patch_without_product_param(self):
        url =  self.construct_url(self.ACTIVITY_API_WITHOUT_PRODUCT)
        return url

    def url_patch_with_product_param(self):
        url =  self.construct_url(self.ACTIVITY_API_WITH_PRODUCT)
        return url

    def url_patch_with_unexisted_product_param(self):
        url =  self.construct_url(self.ACTIVITY_API_WITH_UNEXISTED_PRODUCT)
        return url

    def body_patch_bom(self):
        f = open(os.path.join( self.root_dir(self.files_dir), 'body_with_all_attributes.json'))
        body = json.load(f)
        return body

    def body_without_required_sku_field(self):
        f = open(os.path.join( self.root_dir(self.files_dir), 'body_with_missed_sku.json'))
        body = json.load(f)
        return body

    def body_without_required_code_field(self):
        f = open(os.path.join( self.root_dir(self.files_dir), 'body_with_missed_code.json'))
        body = json.load(f)
        return body

    def body_with_only_required_field(self):
        f = open(os.path.join( self.root_dir(self.files_dir), 'body_with_only_required_field.json'))
        body = json.load(f)
        return body

    def get_json_schema(self, schema):
        f = open(os.path.join(self.root_dir(self.files_dir), schema))
        json_schema = json.load(f)
        f.close()
        return json_schema

    def patch_500_missed_param_response_is_valid(self, response):
        f = open(os.path.join( self.root_dir(self.files_dir), 'SCHEMA_PATCH_500_MISSED_PARAM.json'))
        json_schema = json.load(f)
        f.close()
        if self.base.validateJson(response.json(), json_schema):
            return 'valid'
        else:
            return 'invalid'

    def patch_500_missed_body_or_required_fields_response_is_valid(self, response):
        f = open(os.path.join( self.root_dir(self.files_dir), 'SCHEMA_PATCH_500_MISSED_BODY_OR_REQUIRED_FIELDS.json'))
        json_schema = json.load(f)
        f.close()
        if self.base.validateJson(response.json(), json_schema):
            return 'valid'
        else:
            return 'invalid'
