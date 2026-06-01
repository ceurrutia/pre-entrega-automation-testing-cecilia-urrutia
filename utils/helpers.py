
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json


def get_driver():
    options = Options()
    #descativa las contrasenias y notificaciones en elrt del navegador
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

##CSV

def load_user_csv(path):
    users = []
    
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row["username"] and row["password"]:  
                users.append((row["username"], row["password"]))
    return users

##JSON 

def load_user_json( path ):
    users = []
    
    with open(path) as file:
        data = json.load(file)
        
        for user in data: 
                users.append((user["username"], user["password"]))
    return users
        