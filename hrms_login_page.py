import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def hrms_login_page():
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    xpath_for_username = "//input[@placeholder='Username']"
    xpath_for_password = "//input[@placeholder='Password']"
    xpath_for_submit = "//button[@type='submit']"

    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_username )))
    username = driver.find_element(By.XPATH, xpath_for_username)
    username.send_keys("Admin")
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_for_password)))
    password = driver.find_element(By.XPATH, xpath_for_password)
    password.send_keys("admin123")
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_for_submit)))
    submit = driver.find_element(By.XPATH, xpath_for_submit)
    submit.click()
    time.sleep(2)
    driver.quit()

hrms_login_page()