import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_hrms_login_page():
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    username.send_keys("Admin")

    password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    password.send_keys("admin123")

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit.click()

    time.sleep(2)
    driver.quit()
