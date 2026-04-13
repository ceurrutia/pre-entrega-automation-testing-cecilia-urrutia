from selenium import webdriver

def test_prueba():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    
    driver.quit()