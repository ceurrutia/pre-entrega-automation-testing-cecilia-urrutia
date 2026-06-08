from api.api_clients import create_user, create_user, get_users
from conftest import user_data

def test_get_user():
    response = get_users()
    if response.status_code == 200:
        print(response.json())
    
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0


##creatre
def test_create_user(user_data):
    response = create_user(user_data["name"], user_data["job"])
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "lider de la nabucodonosor"