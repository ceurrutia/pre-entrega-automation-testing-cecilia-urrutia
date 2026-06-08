from api.api_clients import create_user, create_user, delete_user, get_all_users, get_users, update_user
from conftest import user_data

##obtiene

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
    

##update

def test_update_user(user_data):
    response = create_user(user_data["name"], user_data["job"])
    assert response.status_code == 201
    user_id = response.json()["id"]
    
    updated_response = update_user(user_id, "Neo", "El elegido")
    assert updated_response.status_code == 200
    assert updated_response.json()["name"] == "Neo"
    assert updated_response.json()["job"] == "El elegido"

    
#deletea

def test_delete_user(user_data):
    response = create_user(user_data["name"], user_data["job"])
    assert response.status_code == 201
    user_id = response.json()["id"]
    
    delete_response = delete_user(user_id)
    assert delete_response.status_code == 204
    
    
## obtiene todos

def test_get_all_users():
    response = get_all_users()
    if response.status_code == 200:
        print(response.json())
    
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0