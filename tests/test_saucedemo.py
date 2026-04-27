from selenium import webdriver
from selenium.webdriver.common.by import By

def test_prueba():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    
    driver.quit()
    
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    
    assert "inventory" in driver.current_url
    
    driver.quit()   