import os
from ProductAPI.base import Base
import json
from ProductAPI.files import GET_retrieve


class GetRetrieveMethods(Base):
    ACTIVITY_API_WITH_PRODUCT = "/product/320010"
    ACTIVITY_API_WITH_UNEXISTED_PRODUCT = "/product/320000"
    ACTIVITY_API_WITHOUT_PRODUCT = "/product"
    files_dir = GET_retrieve

    def url_get_without_product_param(self):
        url = self.construct_url(self.ACTIVITY_API_WITHOUT_PRODUCT)
        return url

    def url_get_with_product_param(self):
        url = self.construct_url(self.ACTIVITY_API_WITH_PRODUCT)
        return url

    def url_get_with_unexisted_product_param(self):
        url = self.construct_url(self.ACTIVITY_API_WITH_UNEXISTED_PRODUCT)
        return url

    def get_json_schema(self, schema):
        f = open(os.path.join(self.root_dir(self.files_dir), schema))
        json_schema = json.load(f)
        f.close()
        return json_schema

