import requests
from behave import when, then



@when("I send a request to list posts")
def step_when_list_posts(context):
    # JSONPlaceholder demo API
    context.response = requests.get("https://jsonplaceholder.typicode.com/posts")


@then("the API should return status code 200")
def step_then_status_code(context):
    assert context.response.status_code == 200, \
        f"Expected 200, got {context.response.status_code}"


@then("the response should contain a list of posts")
def step_then_posts_list(context):
    body = context.response.json()
    assert isinstance(body, list), f"Expected a list, got: {type(body)}"
    assert len(body) > 0, "Expected at least one post in the list"
