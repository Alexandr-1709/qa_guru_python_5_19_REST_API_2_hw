import requests
from jsonschema.validators import validate
from datetime import datetime

from helper import load_json_schema, reqres_session


def test_single_user_not_found_schema_validation():
    schema = load_json_schema('get_single_user_not_found.json')

    response = reqres_session.get('/api/users/13')

    validate(instance=response.json(), schema=schema)


def test_get_users_list_schema_validation():
    page = 2
    schema = load_json_schema('get_users_list.json')

    response = reqres_session.get("/api/users", params={"page": page})
    validate(instance=response.json(), schema=schema)


def test_create_user_with_current_date():
    cur_date = datetime.now().date()
    payload = {"name": "morpheus",
               "job": "leader"}

    response = reqres_session.post("/api/users", json=payload)

    assert response.status_code == 201
    assert datetime.strptime(response.json()['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ').date() == cur_date


def test_create_user_schema_validation():
    pyload = {"name": "Aleksandr",
               "job": "engineer"}
    schema = load_json_schema('post_create_user.json')

    response = reqres_session.post("/api/users", json=pyload)

    validate(instance=response.json(), schema=schema)


def test_put_update_user_schema_validation():
    pyload = {"name": "Aleksandr",
               "job": "AutomationQA"}

    schema = load_json_schema('put_update_user.json')

    response = reqres_session.put("/api/users/21", json=pyload)

    validate(instance=response.json(), schema=schema)


def test_delete_user():

    response = reqres_session.delete("/api/users/21")

    assert response.status_code == 204
    assert response.headers['Content-Length'] == '0'


def test_register_successful_schema_validation():
    pyload = {"email": "eve.holt@reqres.in",
              "password": "pistol"}
    schema = load_json_schema('post_register_successful.json')

    response = reqres_session.post('/api/register', json=pyload)

    validate(instance=response.json(), schema=schema)


def test_register_unsuccessful_schema_validation():
    pyload = {"email": "sydney@fife"}
    schema = load_json_schema('post_register_unsuccessful.json')

    response = reqres_session.post('/api/register', json=pyload)

    validate(instance=response.json(), schema=schema)


def test_login_successful_schema_validation():
    pyload = {"email": "eve.holt@reqres.in",
              "password": "cityslicka"}
    schema = load_json_schema('post_login_successful.json')

    response = reqres_session.post('/api/login', json=pyload)

    validate(instance=response.json(), schema=schema)


def test_login_unsuccessful_schema_validation():
    pyload = {"email": "eve.holt@reqres.in"}
    schema = load_json_schema('post_login_unsuccessful.json')

    response = reqres_session.post('/api/login', json=pyload)

    validate(instance=response.json(), schema=schema)


def test_get_single_user_schema_validation():
    schema = load_json_schema('get_single_user.json')

    response = reqres_session.get('/api/users/2')

    validate(instance=response.json(), schema=schema)


def test_get_list_resources_schema_validation():
    schema = load_json_schema("get_list_resources.json")

    response = reqres_session.get('/api/unknown')

    validate(instance=response.json(), schema=schema)
