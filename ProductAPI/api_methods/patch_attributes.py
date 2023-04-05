import os
from ProductAPI.base import Base
import json
from ProductAPI.files import PATCH_attributes


class PatchAttributesMethods(Base):
    ACTIVITY_API_WITH_PRODUCT = "/product/320010/attributes"
    ACTIVITY_API_WITH_UNEXISTED_PRODUCT = "/product/320000/attributes"
    ACTIVITY_API_WITHOUT_PRODUCT = "/product/attributes"
    files_dir = PATCH_attributes

    def url_patch_without_product_param(self):
        url = self.construct_url(self.ACTIVITY_API_WITHOUT_PRODUCT)
        return url

    def url_patch_with_product_param(self):
        url = self.construct_url(self.ACTIVITY_API_WITH_PRODUCT)
        return url

    def url_patch_with_unexisted_product_param(self):
        url = self.construct_url(self.ACTIVITY_API_WITH_UNEXISTED_PRODUCT)
        return url

    def body_patch_attributes(self):
        f = open(os.path.join(self.root_dir(self.files_dir), 'body_with_all_attributes.json'))
        body = json.load(f)
        f.close()
        return body

    def body_without_required_fields_attributes(self):
        f = open(os.path.join(self.root_dir(self.files_dir), 'body_without_required_field.json'))
        body = json.load(f)
        f.close()
        return body

    def body_with_only_required_field(self):
        f = open(os.path.join(self.root_dir(self.files_dir), 'body_with_only_required_field.json'))
        body = json.load(f)
        f.close()
        return body

    def get_json_schema(self, schema):
        f = open(os.path.join(self.root_dir(self.files_dir), schema))
        json_schema = json.load(f)
        f.close()
        return json_schema

