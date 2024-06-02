import requests
import allure
import data.test_data
from data.variables import data_without_required_field
from data.urls import creating_user


class TestCreatingUser:

    @allure.title('Создание уникального пользователя')
    def test_creating_unique_user(self):
        random_user_data = data.test_data.random_user_data()
        response = requests.post(creating_user, data=random_user_data)
        assert 200 == response.status_code and response.json()["success"]

    @allure.title('Создание зарегистрированного пользователя')
    def test_creating_registered_user(self):
        payload_registered_user = data.test_data.payload_registered_user()
        response = requests.post(creating_user, data=payload_registered_user)
        assert "User already exists" == response.json()["message"] and 403 == response.status_code

    @allure.title('Создание пользователя без обязательного поля')
    def test_creating_user_without_field(self):
        response = requests.post(creating_user, data=data_without_required_field)
        assert "Email, password and name are required fields" == response.json()[
            "message"] and 403 == response.status_code
