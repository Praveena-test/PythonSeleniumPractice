from selenium import webdriver
import allure
import pytest

@allure.title("Verify the title of the app.vwo page")
def test_vwo_login():
    driver = webdriver.Chrome()
    # Here we are actually making POST request to open Chrome driver
    # Session-ID will be created

    driver.get("https://app.vwo.com")
    # Here we are actually making get request to Chrome driver(through selenium manger)
    # using the session-id
    assert driver.title == "Login - VWO"

    # driver.title is a get request which gets the title of the login page.