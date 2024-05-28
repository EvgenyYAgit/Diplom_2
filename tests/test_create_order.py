import requests
import allure
from date.urls import creating_order
from date.variables import ingred_burger, two_inredients


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_with_authorization(self, headers_registered_user):
        ingredient = {"ingredients": [ingred_burger]}
        response = requests.post(creating_order, headers=headers_registered_user, data=ingredient)
        assert "Gintama" == response.json()["order"]["owner"]["name"] and 200 == response.status_code

    @allure.title('Создание заказа без авторизации')
    def test_without_authorization(self):
        ingredient = {"ingredients": [ingred_burger]}
        response = requests.post(creating_order, data=ingredient)
        assert "Флюоресцентный бургер" == response.json()["name"] and 200 == response.status_code

    @allure.title('Создание заказа с ингредиентами')
    def test_with_ingredients(self):
        ingredients = {"ingredients": two_inredients}
        response = requests.post(creating_order, data=ingredients)
        assert response.json()["success"] and 200 == response.status_code

    @allure.title('Создание заказа без ингредиентов')
    def test_without_ingredients(self):
        response = requests.post(creating_order)
        assert "Ingredient ids must be provided" == response.json()["message"] and 400 == response.status_code

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_with_incorrect_ingredient_hash(self):
        ingredient = {"ingredients": ["nothing"]}
        response = requests.post(creating_order, data=ingredient)
        assert 500 == response.status_code
