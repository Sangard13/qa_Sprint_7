class TestData:
    # Valid test data
    VALID_COURIER = {
        "login": "ninja_test",
        "password": "1234",
        "firstName": "saske"
    }

    VALID_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uzumaki",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

    # Invalid test data
    INVALID_LOGIN_DATA = [
        {"login": "", "password": "1234"},
        {"login": "ninja", "password": ""},
        {"login": "", "password": ""}
    ]

    INVALID_CREATION_DATA = [
        {"login": "", "password": "1234", "firstName": "saske"},
        {"login": "ninja", "password": "", "firstName": "saske"},
        {"login": "ninja", "password": "1234", "firstName": ""}
    ]
    # Error messages
    ERROR_DUPLICATE_LOGIN = "Этот логин уже используется"
    ERROR_INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"
    ERROR_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
