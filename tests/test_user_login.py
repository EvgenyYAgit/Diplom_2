import requests
import allure
import data.test_data
from data.urls import login_user
from data.variables import incorrect_login_and_password


class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self):
        payload_registered_user = data.test_data.payload_registered_user()
        response = requests.post(login_user, data=payload_registered_user)
        assert 200 == response.status_code and response.json()["success"]

    @allure.title('Логин с неверным логином и паролем')
    def test_login_with_incorrect_login_and_password(self):
        response = requests.post(login_user, data=incorrect_login_and_password)
        assert 401 == response.status_code and "email or password are incorrect" == response.json()["message"]
