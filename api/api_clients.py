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


def apiPost():
    response = requests.post(f"{URL_BASE}/login", headers=HEADERS, json=creds)
    success = response.json()
    print(success['token'])


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