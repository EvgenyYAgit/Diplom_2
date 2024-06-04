import requests
import allure
import data.variables
import data.helpers
from data.urls import creating_order


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_with_authorization(self):
        headers_registered_user = data.helpers.headers_registered_user()
        ingredient = {"ingredients": [data.variables.ingred_burger]}
        response = requests.post(creating_order, headers=headers_registered_user, data=ingredient)
        assert data.variables.name_hero == response.json()["order"]["owner"][
            "name"] and data.variables.ok == response.status_code

    @allure.title('Создание заказа без авторизации')
    def test_without_authorization(self):
        ingredient = {"ingredients": [data.variables.ingred_burger]}
        response = requests.post(creating_order, data=ingredient)
        assert data.variables.name_burger == response.json()["name"] and data.variables.ok == response.status_code

    @allure.title('Создание заказа с ингредиентами')
    def test_with_ingredients(self):
        ingredients = {"ingredients": data.variables.two_inredients}
        response = requests.post(creating_order, data=ingredients)
        assert response.json()["success"] and data.variables.ok == response.status_code

    @allure.title('Создание заказа без ингредиентов')
    def test_without_ingredients(self):
        response = requests.post(creating_order)
        assert data.variables.text_bad_request == response.json()[
            "message"] and data.variables.bad_request == response.status_code

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_with_incorrect_ingredient_hash(self):
        ingredient = {"ingredients": ["nothing"]}
        response = requests.post(creating_order, data=ingredient)
        assert data.variables.internal_server_error == response.status_code
