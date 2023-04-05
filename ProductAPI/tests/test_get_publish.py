import pytest
import requests
from ProductAPI.api_methods.get_publish import GetPublishMethods
from ProductAPI.base import Base

class TestGetPublish(GetPublishMethods):
    getPublish = GetPublishMethods()

    @pytest.mark.smoke_tests
    @pytest.mark.get_publish_positive_tests
    def test_successful_response_received(self):
        response = requests.get(url=self.getPublish.url_get_with_all_params())
        assert response.status_code == 202, \
            "Got wrong status code, expected is: {}, actual is  {}".format("202", response.status_code)

    @pytest.mark.get_publish_negative_tests
    @pytest.mark.parametrize('url', [getPublish.url_get_without_all_params(),
                                     getPublish.url_get_without_time(),
                                     getPublish.url_get_without_to_time(),
                                     getPublish.url_get_without_from_time(),
                                     getPublish.url_get_without_stream()])
    def test_error_received_when_some_params_are_missed(self, url):
        response = requests.get(url=url)
        print(response.json())
        assert response.status_code == 400, \
            "Got wrong status code, expected is: {}, actual is  {}".format("400", response.status_code)
        assert self.validateJson(response.json(), self.get_json_schema("SCHEMA_GET_PUBLISH_400_BAD_REQUEST.json")) is True, \
            "Response doesn't correspond json Schema"
        assert response.json()["errorCategory"] == \
               "User validation failed", "errorCategory must be User validation failed"
        assert response.json()["responseCode"] == \
               "typeMismatch", "responseCode must be typeMismatch"
