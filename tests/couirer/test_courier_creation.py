import pytest
from data.test_data import TestData
from utils.helpers import Helpers


class TestCourierCreation:

    @pytest.mark.smoke
    @pytest.mark.courier
    def test_create_courier_success(self, courier_api, courier_data):
        """Тест успешного создания курьера"""
        response = courier_api.create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["firstName"]
        )

        Helpers.check_response_status(response, 201)
        response_data = Helpers.extract_json(response)
        assert response_data.get("ok") == True

        login_response = courier_api.login_courier(
            courier_data["login"],
            courier_data["password"]
        )
        Helpers.check_response_status(login_response, 200)

        courier_id = login_response.json().get("id")
        assert courier_id is not None, "Courier ID should not be None"

        delete_response = courier_api.delete_courier(courier_id)
        Helpers.check_response_status(delete_response, 200)

    @pytest.mark.regression
    @pytest.mark.courier
    @pytest.mark.parametrize("invalid_data", TestData.INVALID_CREATION_DATA)
    def test_create_courier_missing_data(self, courier_api, invalid_data):
        """Тест создания курьера с недостаточными данными"""
        response = courier_api.create_courier(
            invalid_data.get("login", ""),
            invalid_data.get("password", ""),
            invalid_data.get("firstName", "")
        )

        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для создания учетной записи")

    @pytest.mark.regression
    @pytest.mark.courier
    def test_create_duplicate_courier(self, create_and_delete_courier, courier_api):
        """Тест создания курьера с дублирующимся логином"""
        courier_data, courier_id = create_and_delete_courier

        # Пытаемся создать курьера с тем же логином
        response = courier_api.create_courier(
            courier_data["login"],
            "different_password",
            "different_name"
        )

        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для создания учетной записи")