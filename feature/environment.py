from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage

def before_all(context):
    pass

def before_scenario(context, scenario):
    service = Service()
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    
    #inicializa el login page 
    context.login_page = LoginPage(context.driver)

#cerramos despues de cada scenario
def after_scenario(context, scenario):
    context.driver.quit()