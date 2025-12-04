@ui
Feature: SauceDemo Login

  @smoke @fast
  Scenario: Verify homepage logo is present
    When open saucedemo homepage
    Then verify homepage title 'Swag Labs' is present

  @regression @slow
  Scenario Outline: Login with different users
    Given I am on the SauceDemo login page
    When I login with username "<username>" and password "<password>"
    And I click on the login button
    Then I should see "<expected>" result

    Examples:
      | username        | password      | expected        |
      | standard_user   | secret_sauce  | Products page   |
      | standard_user   | wrong_pass    | Epic sadface    |
