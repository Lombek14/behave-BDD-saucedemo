from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    """Setup before each scenario based on tags"""
    
    # Only start browser for UI scenarios
    if "ui" in scenario.effective_tags:
        options = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        context.driver.implicitly_wait(5)
        context.driver.maximize_window()

    # Setup for API scenarios  
    if "api" in scenario.effective_tags:
        context.base_url = "https://jsonplaceholder.typicode.com"
        context.headers = {"Content-Type": "application/json"}


def after_scenario(context, scenario):
    """Cleanup after each scenario"""
    
    # Close browser if it was opened
    if hasattr(context, "driver"):
        context.driver.quit()