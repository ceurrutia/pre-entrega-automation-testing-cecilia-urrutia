import pytest
import time
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    ##pregunte a geminis como escaparme del alert que dice que la contrasenia es insegura
    #chrome_options.add_argument("--headless") #Para CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    time.sleep(1) #un time para ver el resultado
    driver.quit()
    
@pytest.fixture
def user_data():
   return {
       "name": "morpheus",
       "job": "lider de la nabucodonosor"
}
   
   
##corer reports con pytest -v --html=reports/report.html --self-contained-html
   
##Titlo de los reprtes
def pytest_html_report_title(report):
    report.title = "API - UI Pytest Selenium"
    
    
##crear las capturas de pantala 
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        
        if driver:
           driver.save_screenshot(f"reports/screenshots/{item.name}.png") #nombre de la captura
           