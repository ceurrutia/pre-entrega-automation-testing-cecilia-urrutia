
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json


def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
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
        