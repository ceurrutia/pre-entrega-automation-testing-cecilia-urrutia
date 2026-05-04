from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.commons.funciones_commons import login, logout

def test_title(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    
    
def test_url_inventario(driver):
    driver.get("https://www.saucedemo.com/")
    login(driver)
    if "inventory" in driver.current_url:
        print("Test ok")
    else:
        print("Test fallido")



def test_logout(driver):
    driver.get("https://www.saucedemo.com/")
    login(driver)
    logout(driver)
    


def test_titulo_despues_de_login(driver):
    driver.get("https://www.saucedemo.com/")
    login(driver)
    
    wait = WebDriverWait(driver, 10)
    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    ).text
    
    assert titulo == "Products", f"Se esperaba 'Products' pero se encontro '{titulo}'"
    

def test_agregar_producto_a_carrito(driver):
    driver.get("https://www.saucedemo.com/")
    login(driver)
    
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    
    cart_count = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text
    
    assert cart_count == "1", f"Se esperaba 1 en el carrito pero encontro {cart_count}"