import requests
import allure
import data.helpers
import data.variables
from data.urls import get_order


class TestReceivingUserOrders:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_authorized_user(self):
        headers_registered_user = data.helpers.headers_registered_user()
        response = requests.get(get_order, headers=headers_registered_user)
        assert response.json()["success"] and data.variables.ok == response.status_code

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_unauthorized_user(self):
        response = requests.get(get_order)
        assert data.variables.text_unauthorized == response.json()[
            "message"] and data.variables.unauthorized == response.status_code
