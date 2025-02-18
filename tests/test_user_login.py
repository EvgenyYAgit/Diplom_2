import requests
import allure
from data.test_data import payload_registered_user
import data.variables
from data.urls import login_user
from data.variables import incorrect_login_and_password


class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_existing_user(self):
        response = requests.post(login_user, data=payload_registered_user)
        assert data.variables.ok == response.status_code and response.json()["success"]

    @allure.title('Логин с неверным логином и паролем')
    def test_login_with_incorrect_login_and_password(self):
        response = requests.post(login_user, data=incorrect_login_and_password)
        assert data.variables.unauthorized == response.status_code and data.variables.text_unauthorized_incorrect == \
               response.json()["message"]
