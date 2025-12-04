from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# Scenario 1
@when("open saucedemo homepage")
def open_homepage(context):
    context.driver.get("https://www.saucedemo.com/")


@then("verify homepage title 'Swag Labs' is present")
def logo(context):
    logo_element = context.driver.find_element(By.CLASS_NAME, "login_logo")
    assert logo_element.is_displayed(), "Logo is not displayed"


# Scenario 2
@given('I am on the SauceDemo login page')
def login(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I login with username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)


@when('I click on the login button')
def click_login_button(context):
    print("\n>>> CLICKING LOGIN BUTTON <<<")
    context.driver.find_element(By.ID, "login-button").click()


@then('I should see the products page')
def see_home_page(context):
    Products_element: WebElement = context.driver.find_element(By.CLASS_NAME, "title")
    assert Products_element.text == "Products"