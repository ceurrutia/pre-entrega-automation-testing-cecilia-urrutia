import pytest
from pages.login_page import LoginPage
from pages.login_page import login_completo
from utils.helpers import load_user_csv, load_user_json
from data.users import USERS    
from faker import Faker

##data driven test
load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")
fake = Faker()


@pytest.mark.parametrize("username,password", load_csv) 
def test_login(driver, username, password):
    login_page = LoginPage(driver)
    
    login_completo()
    
    # name = fake.name()
    # first_name = fake.first_name()
    # last_name = fake.last_name()
    # email = fake.email()    
    # codigo_postal = fake.postcode()
    
    
    # print(":Datos generados por Faker", name, first_name, last_name, email, codigo_postal)