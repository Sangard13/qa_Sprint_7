import pytest
from data.test_data import TestData
from utils.helpers import Helpers


class TestCourierLogin:

    @pytest.mark.smoke
    @pytest.mark.courier
    def test_login_success(self, create_and_delete_courier, courier_api):
        """Тест успешного логина курьера"""
        courier_data, courier_id = create_and_delete_courier

        response = courier_api.login_courier(
            courier_data["login"],
            courier_data["password"]
        )

        Helpers.check_response_status(response, 200)
        response_data = Helpers.extract_json(response)
        assert "id" in response_data
        assert isinstance(response_data["id"], int)

    @pytest.mark.regression
    @pytest.mark.courier
    @pytest.mark.parametrize("invalid_data", TestData.INVALID_LOGIN_DATA)
    def test_login_missing_data(self, courier_api, invalid_data):
        """Тест логина с недостаточными данными"""
        response = courier_api.login_courier(
            invalid_data.get("login", ""),
            invalid_data.get("password", "")
        )

        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для входа")

    @pytest.mark.regression
    @pytest.mark.courier
    def test_login_wrong_credentials(self, courier_api):
        """Тест логина с неверными учетными данными"""
        response = courier_api.login_courier("nonexistent", "wrongpassword")

        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для входа")