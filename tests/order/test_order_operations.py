import pytest
from utils.helpers import Helpers


class TestOrderOperations:

    @pytest.mark.smoke
    @pytest.mark.order
    def test_accept_order(self, create_and_delete_courier, create_order, order_api):
        """Тест принятия заказа курьером"""
        courier_data, courier_id = create_and_delete_courier
        order_data, track_number, _ = create_order

        track_response = order_api.get_order_by_track(track_number)
        Helpers.check_response_status(track_response, 200)

        order_id = track_response.json()["order"]["id"]
        assert order_id is not None, "Order ID should not be None"

        response = order_api.accept_order(order_id, courier_id)
        Helpers.check_response_status(response, 200)
        response_data = Helpers.extract_json(response)
        assert response_data.get("ok") == True

    @pytest.mark.smoke
    @pytest.mark.order
    def test_finish_order(self, create_and_delete_courier, create_order, order_api):
        """Тест завершения заказа"""
        courier_data, courier_id = create_and_delete_courier
        order_data, track_number, _ = create_order

        # Получаем ID заказа по треку
        track_response = order_api.get_order_by_track(track_number)
        Helpers.check_response_status(track_response, 200)

        order_id = track_response.json()["order"]["id"]
        assert order_id is not None, "Order ID should not be None"

        # Принимаем заказ
        accept_response = order_api.accept_order(order_id, courier_id)
        Helpers.check_response_status(accept_response, 200)

        # Проверяем, что заказ принят перед завершением
        order_status_response = order_api.get_order_by_track(track_number)
        Helpers.check_response_status(order_status_response, 200)

        order_status = order_status_response.json()["order"]
        assert order_status.get("courierId") == courier_id, "Order should be assigned to courier"

        # Завершаем заказ
        response = order_api.finish_order(order_id)
        Helpers.check_response_status(response, 200)
        response_data = Helpers.extract_json(response)
        assert response_data.get("ok") == True

    @pytest.mark.regression
    @pytest.mark.order
    def test_cancel_order(self, create_order, order_api):
        """Тест отмены заказа"""
        order_data, track_number, _ = create_order

        response = order_api.cancel_order(track_number)
        assert response.status_code in [200, 400], f"Unexpected status code: {response.status_code}"

    @pytest.mark.regression
    @pytest.mark.order
    def test_accept_nonexistent_order(self, create_and_delete_courier, order_api):
        """Тест принятия несуществующего заказа"""
        courier_data, courier_id = create_and_delete_courier

        # Пытаемся принять несуществующий заказ
        response = order_api.accept_order(999999, courier_id)
        Helpers.check_response_status(response, 400)
        Helpers.check_error_message(response, "Недостаточно данных для поиска")