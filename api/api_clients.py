import requests
import os

##Dotenv
from dotenv import load_dotenv

load_dotenv()

URL_BASE = "https://reqres.in/api"

HEADERS = {
    "X-api-key": os.getenv("X_API_KEY"),
    "Content-Type": "application/json"
    }

creds ={
    'email': os.getenv('EMAIL_USER'),
    'password': os.getenv('PASSWORD_USER')
}

def get_users():
    response = requests.get(f"{URL_BASE}/users", headers=HEADERS)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
    return response

##todos

def get_all_users():
    response = requests.get(f"{URL_BASE}/users?page=2", headers=HEADERS)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
    return response


###############post a la api###############
def apiPost():
    response = requests.post(f"{URL_BASE}/login", headers=HEADERS, json=creds)
    success = response.json()
    print(success['token'])

###############create########################

def create_user(name, job):
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(f"{URL_BASE}/users", headers=HEADERS, json=payload)
    if response.status_code == 201:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
    return response

###############update####################

def update_user(user_id, name, job):
    payload = {
        "name": name,
        "job": job
    }
    response = requests.put(f"{URL_BASE}/users/{user_id}", headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
    return response



################delete#######################

def delete_user(user_id):
    response = requests.delete(f"{URL_BASE}/users/{user_id}", headers=HEADERS)
    if response.status_code == 204:
        print("Usuario eliminado correctamente")
    else:
        print(f"Error: {response.status_code}")
    return response