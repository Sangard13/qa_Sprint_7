import sys
import os
import requests
import pytest
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from api.courier_api import CourierAPI
from api.order_api import OrderAPI
from utils.generators import DataGenerator
from utils.helpers import Helpers


@pytest.fixture
def courier_api():
    return CourierAPI()


@pytest.fixture
def order_api():
    return OrderAPI()


@pytest.fixture
def courier_data():
    return DataGenerator.generate_courier_data()


@pytest.fixture
def order_data():
    return DataGenerator.generate_order_data()


@pytest.fixture
def create_and_delete_courier(courier_api, courier_data):
    """Фикстура для создания и последующего удаления курьера"""
    # Создаем курьера
    response = courier_api.create_courier(
        courier_data["login"],
        courier_data["password"],
        courier_data["firstName"]
    )

    Helpers.check_response_status(response, 201)

    # Логинимся чтобы получить ID
    login_response = courier_api.login_courier(
        courier_data["login"],
        courier_data["password"]
    )
    Helpers.check_response_status(login_response, 200)

    courier_id = login_response.json().get("id")
    assert courier_id is not None, "Courier ID should not be None"

    yield courier_data, courier_id

    # Удаляем курьера после теста
    delete_response = courier_api.delete_courier(courier_id)
    assert delete_response.status_code in [200, 400], f"Delete failed with status {delete_response.status_code}"


@pytest.fixture
def create_order(order_api, order_data):
    """Фикстура для создания заказа"""
    response = order_api.create_order(order_data)
    Helpers.check_response_status(response, 201)

    track_number = response.json().get("track")
    assert track_number is not None, "Track number should not be None"

    yield order_data, track_number, response

    # Очистка: пытаемся отменить заказ
    cancel_response = order_api.cancel_order(track_number)