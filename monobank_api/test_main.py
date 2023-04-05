import requests
import pytest
import vcr
from jsonschema import validate

BASIC_URL = "https://api.monobank.ua"
ACTIVITY_API = "/bank/currency"


def construct_url(common_url, api):
    return common_url + api


# ------------------------------------------requests lib-----------------------------------------------------
def test_get_status_code_equals_200():
    url = construct_url(BASIC_URL, ACTIVITY_API)
    response = requests.get(url)
    assert response.status_code == 200, print(
        "Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code))


def test_check_type_in_response_body():
    url = construct_url(BASIC_URL, ACTIVITY_API)
    response = requests.get(url)
    print(response.json())
    assert response.json()['rateBuy'] == int(36.7)


def test_check_content_type_headers():
    url = construct_url(BASIC_URL, ACTIVITY_API)
    response = requests.get(url)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8", \
        print("Got wrong content type in headers, expected is: {}, actual is {}"
              .format("application/json; charset=utf-8", response.headers["Content-Type"]))


# -----------------------------------------------vcr lib----------------------------------------------
@vcr.use_cassette('monobank_api/cassettes/monobank_get.yaml')
def test_get_google_home_page():
    url = construct_url(BASIC_URL, ACTIVITY_API)
    response = requests.get(url)
    assert response.status_code == 200, print(
        "Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code))


# -----------------------------------------------json validator------------------------------------------------
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
    },
    "required": ["name"],
}

schema1 = {
    "type": "object",
    "properties": {
        "currencyCodeA": {"type": "number"},
        "currencyCodeB": {"type": "number"},
        "date": {"type": "number"},
        "rateSell": {"type": "number"},
        "rateBuy": {"type": "number"},
        "rateCross":{"type": "number"}
},
    "required": ["currencyCodeA","currencyCodeB","date", "rateSell", "rateBuy",  "rateCross" ],
}


def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """
    return validate(data, schema_file)

def test_json_validation():
    instance={[
    {
        "currencyCodeA": 840,
        "currencyCodeB": 980,
        "date": 1663276209,
        "rateBuy": 36.65,
        "rateSell": 37.4995
    }
]}
    assert_valid_schema(instance,schema1)
