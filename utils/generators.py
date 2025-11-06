from faker import Faker

fake = Faker('ru_RU')


class DataGenerator:

    @staticmethod
    def generate_courier_data():
        """Генерация данных курьера"""
        return {
            "login": fake.user_name() + str(fake.random_int(1000, 9999)),
            "password": fake.password(length=8),
            "firstName": fake.first_name()
        }

    @staticmethod
    def generate_order_data():
        """Генерация данных заказа"""
        return {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": str(fake.random_int(1, 200)),
            "phone": fake.phone_number(),
            "rentTime": fake.random_int(1, 10),
            "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
            "comment": fake.text(max_nb_chars=50),
            "color": [fake.random_element(["BLACK", "GREY", "RED", "BLUE"])]
        }

    @staticmethod
    def generate_unique_login():
        """Генерация уникального логина"""
        return f"test_courier_{fake.random_int(10000, 99999)}"