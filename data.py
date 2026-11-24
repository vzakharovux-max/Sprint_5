import random


def generate_registration_data():
    random_digits = random.randint(100, 999)
    email = f"vlad_zakharov_59_{random_digits}@yandex.ru"
    password = f"Pass{random_digits}!"
    name = "Влад"
    return name, email, password


class ExistingUser:
    EMAIL = "vlad_zakharov_59_111@yandex.ru"
    PASSWORD = "Password123!"
    NAME = "Влад"
