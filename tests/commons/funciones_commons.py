
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    
    
def logout(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()