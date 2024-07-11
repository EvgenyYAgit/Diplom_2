# ингредиент бургер
ingred_burger = "61c0c5a71d1f82001bdaaa6d"
# два ингредиента
two_inredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
# данные без обязательного поля
data_without_required_field = {
            "password": "1234512345A",
            "name": "Локи"
        }
# неверный логин и пароль
incorrect_login_and_password = {
            "email": "gintam@mail.ru",
            "password": "423782",
            "name": "Gintama"
        }

# тексты ответов
ok = 200
bad_request = 400
unauthorized = 401
forbidden = 403
internal_server_error = 500
text_forbidden_exists = "User already exists"
text_forbidden_requerd = "Email, password and name are required fields"
text_unauthorized = "You should be authorised"
text_unauthorized_incorrect = "email or password are incorrect"
text_bad_request = "Ingredient ids must be provided"
name_hero = "Gintama"
name_burger = "Флюоресцентный бургер"
