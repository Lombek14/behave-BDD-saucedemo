@ui
Feature: SauceDemo Login

  Scenario: Verify homepage logo is present
    When open saucedemo homepage
    Then verify homepage title 'Swag Labs' is present

  Scenario: Successful login with valid user
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    And I click on the login button
    Then I should see the products page

    


