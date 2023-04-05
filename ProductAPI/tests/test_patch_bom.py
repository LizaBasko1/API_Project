import pytest
import requests
from ProductAPI.api_methods.patch_bom import PatchBomMethods


class TestPatchBom(PatchBomMethods):
    patchBomMethods = PatchBomMethods()

    @pytest.mark.patch_bom_positive_tests
    def test_successful_response_received_when_body_has_only_required_field(self):
        response = requests.patch(url=self.url_patch_with_product_param(),
                                  json=self.body_with_only_required_field())
        assert response.status_code == 200, \
            "Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code)

    @pytest.mark.smoke_tests
    @pytest.mark.patch_bom_positive_tests
    def test_successful_response_received_when_body_and_param_is_valid_field(self):
        response = requests.patch(url=self.url_patch_with_product_param(),
                                  json=self.body_patch_bom())
        assert response.status_code == 200, \
            "Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code)

    @pytest.mark.patch_bom_negative_tests
    def test_error_received_when_product_param_is_missed_in_url(self):
        response = requests.patch(url=self.url_patch_without_product_param(),
                                  data=self.body_patch_bom())
        print(response.json())
        assert response.status_code == 500, \
            "Got wrong status code, expected is: {}, actual is  {}".format("500", response.status_code)
        assert self.validateJson(response.json(),
                                 self.get_json_schema("SCHEMA_PATCH_500_MISSED_PARAM.json")) is True, \
            "Response doesn't correspond json Schema"
        assert response.json()['status'] == 500, \
            'Status code in response body is not 500'
        assert response.json()['error'] == 'Internal Server Error', \
            'Error in response body is not Internal Server Error'
        assert response.json()['message'] == "Request method 'PATCH' not supported", \
            "Message in response body is not Request method 'PATCH' not supported"

    @pytest.mark.patch_bom_negative_tests
    def test_error_received_when_body_is_missed(self):
        response = requests.patch(url=self.url_patch_with_product_param())
        assert response.status_code == 500, \
            "Got wrong status code, expected is: {}, actual is  {}".format("500", response.status_code)
        assert self.validateJson(response.json(),
                                 self.get_json_schema("SCHEMA_PATCH_500_MISSED_BODY_OR_REQUIRED_FIELDS.json")) is True, \
            "Response doesn't correspond json Schema"
        assert response.json()['responseCode'] == '500', \
            'Status code in response body is not 500'

    @pytest.mark.patch_bom_negative_tests
    def test_error_received_when_product_param_and_body_are_missed(self):
        response = requests.patch(url=self.url_patch_without_product_param())
        print(response.json())
        assert response.status_code == 500, \
            "Got wrong status code, expected is: {}, actual is  {}".format("500", response.status_code)
        assert self.validateJson(response.json(),
                                 self.get_json_schema("SCHEMA_PATCH_500_MISSED_PARAM.json")) is True, \
            "Response doesn't correspond json Schema"
        assert response.json()['status'] == 500, \
            'Status code in response body is not 500'
        assert response.json()['error'] == 'Internal Server Error', \
            'Error in response body is not Internal Server Error'
        assert response.json()['message'] == "Request method 'PATCH' not supported", \
            "Message in response body is not Request method 'PATCH' not supported"

    @pytest.mark.patch_bom_negative_tests
    def test_error_received_when_productid_does_not_exist(self):
        response = requests.patch(url=self.url_patch_with_unexisted_product_param(),
                                  json=self.body_patch_bom())
        assert response.status_code == 404, \
            "Got wrong status code, expected is: {}, actual is  {}".format("404", response.status_code)

    @pytest.mark.patch_bom_negative_tests
    @pytest.mark.parametrize('body', [patchBomMethods.body_without_required_code_field(),
                                      patchBomMethods.body_without_required_sku_field()])
    def test_error_response_received_when_body_without_required_code_field(self, body):
        response = requests.patch(url=self.url_patch_with_product_param(),
                                  json=body)
        assert response.status_code == 500, \
            "Got wrong status code, expected is: {}, actual is  {}".format("400", response.status_code)
        assert self.validateJson(response.json(),
                                 self.get_json_schema("SCHEMA_PATCH_500_MISSED_BODY_OR_REQUIRED_FIELDS.json")) is True, \
            "Response doesn't correspond json Schema"

