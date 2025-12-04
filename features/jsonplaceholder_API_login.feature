@api
Feature: Posts API

  Scenario: Get list of posts successfully
    When I send a request to list posts
    Then the API should return status code 200
    And the response should contain a list of posts
