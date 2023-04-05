import pytest
from ProductAPI.api_methods.patch_bom import PatchBomMethods

class Fixtures:
    @pytest.fixture
    def body_without_required_code_field(self):
        patchBom = PatchBomMethods()
        body = patchBom.body_without_required_code_field()
        return body

    @pytest.fixture
    def body_without_required_sku_field(self):
        patchBom = PatchBomMethods()
        body = patchBom.body_without_required_sku_field()
        return body