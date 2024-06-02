import requests
from data.generate_unique_user import generate_unique_data
from data.urls import creating_user, login_user


def payload_registered_user():
    payload = {
        "email": "gintama@mail.ru",
        "password": "423782",
        "name": "Gintama"
    }
    return payload


def headers_registered_user():
    payload_login = {
        "email": "gintama@mail.ru",
        "password": "423782",
        "name": "Gintama"
    }
    login = requests.post(login_user, data=payload_login)
    auth_token = login.json()["accessToken"]
    headers = {
        'Authorization': f'{auth_token}'
    }
    return headers


def random_user_data():
    user_data = generate_unique_data()
    payload = {
        "email": f'{user_data[0]}',
        "password": f'{user_data[1]}',
        "name": f'{user_data[2]}'
    }
    return payload


def auth_token_and_random_user_data():
    user_data = generate_unique_data()
    create = {
        "email": f'{user_data[0]}',
        "password": f'{user_data[1]}',
        "name": f'{user_data[2]}'
    }
    create_user = requests.post(creating_user, data=create)
    auth_token = create_user.json()["accessToken"]
    headers = {
        'Authorization': f'{auth_token}'
    }
    return headers, user_data
