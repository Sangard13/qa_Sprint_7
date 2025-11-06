import pytest
from utils.helpers import Helpers


class TestOrderList:

    @pytest.mark.smoke
    @pytest.mark.order
    def test_get_orders_list_default(self, order_api):
        """Тест получения списка заказов с параметрами по умолчанию"""
        response = order_api.get_orders_list()

        Helpers.check_response_status(response, 200)
        response_data = Helpers.extract_json(response)

        assert "orders" in response_data
        assert "pageInfo" in response_data
        assert "availableStations" in response_data

        page_info = response_data["pageInfo"]
        assert page_info["page"] == 0
        assert page_info["limit"] == 30

    @pytest.mark.order
    def test_get_orders_list_with_courier_id(self, create_and_delete_courier, order_api):
        """Тест получения списка заказов с courierId"""
        courier_data, courier_id = create_and_delete_courier

        response = order_api.get_orders_list(courier_id=courier_id)

        Helpers.check_response_status(response, 200)
        response_data = Helpers.extract_json(response)

        assert "orders" in response_data

    @pytest.mark.order
    def test_get_orders_list_with_limit(self, order_api):
        """Тест получения списка заказов с ограничением количества"""
        response = order_api.get_orders_list(limit=5)

        Helpers.check_response_status(response, 200)
        response_data = Helpers.extract_json(response)

        page_info = response_data["pageInfo"]
        assert page_info["limit"] == 5
        assert len(response_data["orders"]) <= 5

    @pytest.mark.order
    def test_get_orders_list_with_pagination(self, order_api):
        """Тест пагинации списка заказов"""
        response_page_0 = order_api.get_orders_list(limit=5, page=0)
        Helpers.check_response_status(response_page_0, 200)

        response_page_1 = order_api.get_orders_list(limit=5, page=1)
        Helpers.check_response_status(response_page_1, 200)

        orders_page_0 = response_page_0.json()["orders"]
        orders_page_1 = response_page_1.json()["orders"]

        if len(orders_page_0) > 0 and len(orders_page_1) > 0:
            order_ids_page_0 = [order["id"] for order in orders_page_0]
            order_ids_page_1 = [order["id"] for order in orders_page_1]

            assert not set(order_ids_page_0).intersection(order_ids_page_1)

    @pytest.mark.regression
    @pytest.mark.order
    def test_get_orders_list_nonexistent_courier(self, order_api):
        """Тест получения списка заказов с несуществующим courierId"""
        response = order_api.get_orders_list(courier_id=999999)

        Helpers.check_response_status(response, 404)
        response_data = Helpers.extract_json(response)
        assert "message" in response_data
        assert "не найден" in response_data["message"]