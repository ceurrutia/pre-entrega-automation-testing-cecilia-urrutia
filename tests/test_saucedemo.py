from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.commons.funciones_commons import login, logout

def test_title():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    
    
def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    login(driver)
    assert "inventory" in driver.current_url

def test_logout(driver):
    driver.get("https://www.saucedemo.com/")
    login(driver)
    logout(driver)