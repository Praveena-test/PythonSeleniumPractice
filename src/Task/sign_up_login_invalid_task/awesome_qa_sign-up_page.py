# Open - https://awesomeqa.com/ui/index.php?route=account/register
# Fill the form
# Verify that next page give - Your Account Has Been Created!
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_sign_up():
    first_name="Ratan"
    last_name="Tata"
    email="rtata6@gmail.com"
    telephone="1234567890"
    password="Qwerty@123"
    confirm_password="Qwerty@123"

    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    time.sleep(5)
    first_name_element= driver.find_element(By.XPATH, "//input[@id='input-firstname']")
    last_name_element=driver.find_element(By.XPATH,"//input[@id='input-lastname']" )
    email_element=driver.find_element(By.XPATH,"//input[@id='input-email']" )
    telephone_element=driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    password_element=driver.find_element(By.XPATH, "//input[@id='input-password']" )
    confirm_password_element=driver.find_element(By.XPATH, "//input[@id='input-confirm']" )
    first_name_element.send_keys(first_name)
    last_name_element.send_keys(last_name)
    email_element.send_keys(email)
    telephone_element.send_keys(telephone)
    password_element.send_keys(password)
    confirm_password_element.send_keys(confirm_password)
    checkbox_element=driver.find_element(By.XPATH, "//input[@name='agree']")
    if not checkbox_element.is_selected():
            checkbox_element.click()

    submit_element=driver.find_element(By.XPATH, "//input[@value='Continue']")
    submit_element.click()
    current_url = driver.current_url
    print(current_url)
    time.sleep(2)

    assert current_url=="https://awesomeqa.com/ui/index.php?route=account/success"
    expected_headline="Your Account Has Been Created!"
    observed_headline=driver.find_element(By.TAG_NAME,"h1")
    print(observed_headline.text)
    assert observed_headline.text == expected_headline
