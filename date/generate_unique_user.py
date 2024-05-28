import random
import string


# создание уникальных тестовых данных для пользователя
def generate_unique_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    user_data = []

    # генерируем емайл, пароль и имя
    email = generate_random_string(5) + '@' + generate_random_string(5) + '.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    user_data.append(email)
    user_data.append(password)
    user_data.append(name)
    return user_data
