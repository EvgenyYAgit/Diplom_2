import requests
import allure
from data.urls import changing_data
from data.generate_unique_user import generate_unique_data
import data.test_data


class TestChangingUserData:

    @allure.title('Изменение данных name пользователя с авторизацией')
    def test_with_authorization_change_name(self):
        auth_token_and_random_user_data = data.test_data.auth_token_and_random_user_data()
        headers = auth_token_and_random_user_data[0]
        user_data = auth_token_and_random_user_data[1]
        new_user_name = generate_unique_data()
        new_name = new_user_name[2]
        payload = {
            "email": f'{user_data[0]}',
            "password": f'{user_data[1]}',
            "name": f'{new_name}'
        }
        response = requests.patch(changing_data, headers=headers, data=payload)
        assert f'{new_name}' == response.json()["user"]["name"] and 200 == response.status_code

    @allure.title('Изменение данных email пользователя с авторизацией')
    def test_with_authorization_change_email(self):
        auth_token_and_random_user_data = data.test_data.auth_token_and_random_user_data()
        headers = auth_token_and_random_user_data[0]
        user_data = auth_token_and_random_user_data[1]
        new_user_email = generate_unique_data()
        new_email = new_user_email[0]
        payload = {
            "email": f'{new_email}',
            "password": f'{user_data[1]}',
            "name": f'{user_data[2]}'
        }
        response = requests.patch(changing_data, headers=headers, data=payload)
        assert f'{new_email}' == response.json()["user"]["email"] and 200 == response.status_code

    @allure.title('Изменение данных пользователя без авторизации')
    def test_without_authorization(self):
        payload_registered_user = data.test_data.payload_registered_user()
        response = requests.patch(changing_data, data=payload_registered_user)
        assert "You should be authorised" == response.json()["message"] and 401 == response.status_code
