import requests
from behave import *
from jsonschema import validate

post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "id", "title", "body"],
}



@when("I send a request to list posts")
def list_all_posts(context):
    context.response = requests.get(f"{context.base_url}/posts")


@when('I send a GET request to "{endpoint}"')
def get_request(context, endpoint):
    context.response = requests.get(f"{context.base_url}{endpoint}")


@then("the API should return status code {status_code:d}")
def verify_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"


@then("the response should contain a list of posts")
def verify_posts_list(context):
    body = context.response.json()
    assert isinstance(body, list), f"Expected a list, got: {type(body)}"
    assert len(body) > 0, "Expected at least one post in the list"


@then('the response should have field "{field_name}"')
def verify_field_exists(context, field_name):
    body = context.response.json()
    assert isinstance(body, dict), f"Expected a dict, got: {type(body)}"
    assert field_name in body, f"Expected '{field_name}' field in response"

@then("the response should match the posts schema")
def validate_schema(context):
    data = context.response.json()
    validate(instance=data, schema=post_schema)
