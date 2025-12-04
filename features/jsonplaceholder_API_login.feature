@api
Feature: JSONPlaceholder Posts API

  Scenario Outline: Get posts by different IDs
    When I send a GET request to "/posts/<post_id>"
    Then the API should return status code <status_code>
    And the response should have field "id"
    And the response should match the posts schema

    Examples:
      | post_id | status_code |
      | 1       | 200         |
      | 50      | 200         |
      | 100     | 200         |
