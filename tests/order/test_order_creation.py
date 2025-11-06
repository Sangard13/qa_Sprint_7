import pytest
from utils.helpers import Helpers


class TestOrderCreation:

    @pytest.mark.smoke
    @pytest.mark.order
    def test_create_order_success(self, order_api, order_data):
        """Тест успешного создания заказа"""
        response = order_api.create_order(order_data)

        Helpers.check_response_status(response, 201)
        response_data = Helpers.extract_json(response)
        assert "track" in response_data
        assert isinstance(response_data["track"], int)

    @pytest.mark.regression
    @pytest.mark.order
    def test_create_order_with_different_colors(self, order_api, order_data):
        """Тест создания заказа с разными цветами"""
        color_combinations = [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]

        for colors in color_combinations:
            order_data["color"] = colors
            response = order_api.create_order(order_data)

            Helpers.check_response_status(response, 201)
            response_data = Helpers.extract_json(response)
            assert "track" in response_data

    @pytest.mark.smoke
    @pytest.mark.order
    def test_get_order_by_track(self, create_order, order_api):
        """Тест получения заказа по трекингу"""
        order_data, track_number, create_response = create_order

        response = order_api.get_order_by_track(track_number)
        Helpers.check_response_status(response, 200)

        response_data = Helpers.extract_json(response)
        assert "order" in response_data

        order_info = response_data["order"]
        assert order_info["firstName"] == order_data["firstName"]
        assert order_info["lastName"] == order_data["lastName"]
        assert order_info["address"] == order_data["address"]