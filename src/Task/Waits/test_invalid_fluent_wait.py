# [Assignment] - Invalid error message Capture for the Login Page of VWO.com
# Fetch the locators - https://app.vwo.com/
# Create a Python Project
# Add the Allure Report (Allure Pytest)
# Automate the two Test cases of VWO.com
# Invalid Username and Valid Password.
# Capture the error and pass the test.
# Run them and share results
import time
from operator import contains
from os import times

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException, InvalidElementStateException)

def test_invalid_login_check():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"
    invalid_username = "abc@gmail.com"
    invalid_password = "Qwersdfgt"

    username_textbox = driver.find_element(By.XPATH, "//input[@id='login-username']")
    username_textbox.clear()
    username_textbox.send_keys(invalid_username)
    password_textbox = driver.find_element(By.XPATH, "//input[@name='password']")
    password_textbox.clear()
    password_textbox.send_keys(invalid_password)
    login_button = driver.find_element(By.ID, "js-login-btn")
    login_button.click()

    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match
    # </div>
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException,InvalidElementStateException]
    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))
    expected_error_msg = "Your email, password, IP address or location did not match"
    observed_error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    assert observed_error_msg.text == expected_error_msg
    print(observed_error_msg.text)
