import requests
import allure
import data.test_data
from data.urls import get_order


class TestReceivingUserOrders:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_authorized_user(self):
        headers_registered_user = data.test_data.headers_registered_user()
        response = requests.get(get_order, headers=headers_registered_user)
        assert response.json()["success"] and 200 == response.status_code

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_unauthorized_user(self):
        response = requests.get(get_order)
        assert "You should be authorised" == response.json()["message"] and 401 == response.status_code
