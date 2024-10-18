# Create Selenium Script
# Open the URl - https://katalon-demo-cura.herokuapp.com/
# Find and Click on the Make Appointment button
# Verify the URL
# On the Next Page
# Find and Enter the details of the username and password ( web_element.send_keys()
# Click on the Submit button (click()
# Verify the URL change
from ast import Bytes

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

driver = webdriver.Chrome()
# Step-1: Open the URl - https://katalon-demo-cura.herokuapp.com/
driver.get("https://katalon-demo-cura.herokuapp.com/")
assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
#Step-2: Find and Click on the Make Appointment button
make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
make_appointment_element.click()
# Step-3 Verify the URL
assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

#Step 4: On the Next Page,
# Step 5: Find and Enter the details of the username and password ( web_element.send_keys()
demo_username="John Doe"
demo_passwd="ThisIsNotAPassword"

username_textbox = driver.find_element(By.ID, "txt-username")
#<input
# type="text"
# class="form-control"
# id="txt-username"
# name="username"
# placeholder="Username"
# value="" autocomplete="off"
# />
username_textbox.send_keys(demo_username)
password_textbox=driver.find_element(By.ID, "txt-password")
#<input
# type="password"
# class="form-control"
# id="txt-password"
# name="password"
# placeholder="Password"
# value="" autocomplete="off"
# />
password_textbox.send_keys(demo_passwd)


# Step6: Click on the Submit button (click()
login_button=driver.find_element(By.ID, "btn-login")
#login button: <button id="btn-login" type="submit" class="btn btn-default">Login</button>
login_button.click()

# Step 7: Verify the URL change
assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
