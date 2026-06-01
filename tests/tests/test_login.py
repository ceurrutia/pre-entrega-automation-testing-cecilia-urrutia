import pytest
from pages.login_page import LoginPage
from utils.helpers import load_user_csv #, load_user_json
from data.users import USERS    
from faker import Faker

##data driven test
load_csv = load_user_csv("data/users.csv")
# load_json = load_user_json("data/users.json")
fake = Faker()

@pytest.mark.parametrize("username,password", load_csv) 
def test_login(driver, username, password):
    login_page = LoginPage(driver)

    login_page.abrir()
    login_page.login_completo(username, password)
    
    usuarios_exitosos = ["standard_user", "problem_user"]

    if username in usuarios_exitosos:
        assert "inventory.html" in driver.current_url
    else:
        #error
        assert login_page.esta_error_visible(), "El mensaje de error no se muestra como se esperaba."
        assert login_page.obtener_mensaje_error() != "", "El mensaje de error está vacío, se esperaba un mensaje descriptivo."