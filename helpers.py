from faker import Faker

fake = Faker()

# Генерируем уникальные данные пользователя
def generate_user_data():

    return {
        "name": fake.name(),
        "email": f"test_{fake.random_int(1000, 9999)}@yandex.ru",
        "password": fake.password()
    }