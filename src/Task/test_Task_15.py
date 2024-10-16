from selenium import webdriver
import allure
import pytest

@allure.title("Verify the title, URL and string details of the katalon page")
def test_vwo_login():
    driver = webdriver.Chrome()
    # Here we are actually making POST request to open Chrome driver
    # Session-ID will be created

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # Here we are actually making get request to Chrome driver(through selenium manger)
    # using the session-id

    # Verify current title
    expected_title = "CURA Healthcare Service"
    actual_title = driver.title
    assert actual_title == expected_title

    # Verify current URL
    expected_url = "https://katalon-demo-cura.herokuapp.com/"
    actual_url = driver.current_url
    assert actual_url == expected_url

    # Verify if "CURA Healthcare Service" exists in the page source
    page_source = driver.page_source
    assert "CURA Healthcare Service" in page_source
