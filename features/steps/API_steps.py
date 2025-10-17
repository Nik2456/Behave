import requests
from behave import *

API_KEY = 'reqres-free-v1'
HEADERS={"x-api-key": API_KEY}
@given ('i send a Get request to "{url}" with api key')
def i_send_a_get_request(context,url):
    context.response= requests.get(url,headers=HEADERS)
    print("\n=====Response=====")
    print(context.response.text)
    print(context.response.status_code)

@then('response status code should be {status_code:d}')
def the_response_status_code_should_be_200(context,status_code):
    assert context.response.status_code == status_code,f"{context.response.status_code} should be {status_code}"