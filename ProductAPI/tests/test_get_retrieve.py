import pytest
import requests
from ProductAPI.api_methods.get_retrieve import GetRetrieveMethods


class TestGetRetrieve(GetRetrieveMethods):

    @pytest.mark.smoke_tests
    @pytest.mark.get_retrieve_positive_tests
    def test_successful_response_received(self):
        response = requests.get(url=self.url_get_with_product_param())
        assert response.status_code == 200, \
            "Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code)
        assert self.validateJson(response.json(),
                                 self.get_json_schema("SCHEMA_GET_200_OK.json")) is True, \
            "Response doesn't correspond json Schema"

    @pytest.mark.get_retrieve_negative_tests
    def test_error_received_when_product_not_found(self):
        response = requests.get(url=self.url_get_with_unexisted_product_param())
        assert response.status_code == 200, \
            "Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code)
        assert self.validateJson(response.json(),
                                 self.get_json_schema("SCHEMA_GET_200_NOT_FOUND_PRODUCT.json")) is True, \
            "Response doesn't correspond json Schema"
        assert response.json()['responseCode'] == "404", \
            "responseCode is wrong must be 404"
        assert response.json()['status'] == "Product Not Found",\
            "status is wrong must be Product Not Found"

    @pytest.mark.get_retrieve_negative_tests
    def test_error_received_when_product_param_is_missed(self):
        response = requests.get(url=self.url_get_without_product_param())
        assert response.status_code == 404, \
            "Got wrong status code, expected is: {}, actual is  {}".format("404", response.status_code)
        assert self.validateJson(response.json(),
                                 self.get_json_schema("SCHEMA_GET_404_MISSED_PARAM.json")) is True, \
            "Response doesn't correspond json Schema"
        assert response.json()['status'] == 404, \
            "status is wrong must be 404"
        assert response.json()['error'] == "Not Found", \
            "error is wrong must be Not Found"