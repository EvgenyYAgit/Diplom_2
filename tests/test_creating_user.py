import requests
import allure
import data.test_data
import data.variables
from data.urls import creating_user


class TestCreatingUser:

    @allure.title('Создание уникального пользователя')
    def test_creating_unique_user(self):
        random_user_data = data.test_data.random_user_data()
        response = requests.post(creating_user, data=random_user_data)
        assert data.variables.ok == response.status_code and response.json()["success"]

    @allure.title('Создание зарегистрированного пользователя')
    def test_creating_registered_user(self):
        payload_registered_user = data.test_data.payload_registered_user()
        response = requests.post(creating_user, data=payload_registered_user)
        assert data.variables.text_forbidden_exists == response.json()["message"] and data.variables.forbidden == response.status_code

    @allure.title('Создание пользователя без обязательного поля')
    def test_creating_user_without_field(self):
        response = requests.post(creating_user, data=data.variables.data_without_required_field)
        assert data.variables.text_forbidden_requerd == response.json()[
            "message"] and data.variables.forbidden == response.status_code
