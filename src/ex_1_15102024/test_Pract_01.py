from selenium import webdriver
import allure
import pytest

@allure.title("Verify title of the webpage app.vwo.com")
def test_sample():
    driver = webdriver.Edge()
    driver.get("https://www.google.com")
    assert driver.current_url == "https://www.google.com/"