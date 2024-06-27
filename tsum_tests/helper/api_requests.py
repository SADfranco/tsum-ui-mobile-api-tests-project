import requests
import allure
from tsum_tests.utils import attach


def api_get(endpoint, **kwargs):
    with allure.step(f"API GET Request to endpoint {endpoint}"):
        response = requests.get(url="https://api.tsum.ru" + endpoint, **kwargs)

        attach.request_url_and_body(response)
        attach.response_json_and_cookies(response)
        attach.logging_response(response)

        return response


def api_post(endpoint, **kwargs):
    with allure.step(f"API POST Request to endpoint {endpoint}"):
        response = requests.post(url="https://api.tsum.ru" + endpoint, **kwargs)

        attach.request_url_and_body(response)
        attach.response_json_and_cookies(response)
        attach.logging_response(response)

        return response
