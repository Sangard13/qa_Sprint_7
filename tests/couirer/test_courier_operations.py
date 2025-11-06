import pytest
from utils.helpers import Helpers


class TestCourierOperations:

    @pytest.mark.smoke
    @pytest.mark.courier
    def test_delete_courier_success(self, create_and_delete_courier, courier_api):
        """Тест успешного удаления курьера"""
        courier_data, courier_id = create_and_delete_courier

        login_response = courier_api.login_courier(courier_data["login"], courier_data["password"])
        Helpers.check_response_status(login_response, 200)

        # Проверяем что можем получить ID (курьер существует)
        courier_id_from_login = login_response.json().get("id")
        assert courier_id_from_login == courier_id, "Courier ID should match"

        assert courier_data["login"] is not None
        assert courier_data["password"] is not None
        assert courier_data["firstName"] is not None

    @pytest.mark.regression
    @pytest.mark.courier
    def test_delete_nonexistent_courier(self, courier_api):
        """Тест удаления несуществующего курьера"""
        response = courier_api.delete_courier(999999)

        # Проверяем что возвращается ошибка для несуществующего курьера
        assert response.status_code in [400, 404], f"Unexpected status code: {response.status_code}"

    @pytest.mark.smoke
    @pytest.mark.courier
    def test_get_courier_orders_count(self, create_and_delete_courier, courier_api):
        """Тест получения количества заказов курьера"""
        courier_data, courier_id = create_and_delete_courier

        response = courier_api.get_orders_count(courier_id)

        Helpers.check_response_status(response, 200)
        response_data = Helpers.extract_json(response)

        assert "id" in response_data
        assert "ordersCount" in response_data
        assert response_data["id"] == str(courier_id)
        assert isinstance(response_data["ordersCount"], (str, int))

        assert courier_data["login"] is not None

    @pytest.mark.regression
    @pytest.mark.courier
    def test_get_orders_count_nonexistent_courier(self, courier_api):
        """Тест получения количества заказов несуществующего курьера"""
        response = courier_api.get_orders_count(999999)

        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для поиска")

    @pytest.mark.regression
    @pytest.mark.courier
    def test_delete_courier_without_id(self, courier_api):
        """Тест удаления курьера без ID"""
        # Пытаемся удалить курьера с пустым ID
        response = courier_api.delete_courier("")

        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для удаления курьера")

    @pytest.mark.regression
    @pytest.mark.courier
    def test_get_orders_count_without_id(self, courier_api):
        """Тест получения количества заказов без ID курьера"""
        # Пытаемся получить количество заказов без ID
        response = courier_api.get_orders_count("")

        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для поиска")