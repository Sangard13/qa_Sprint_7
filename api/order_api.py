from api.base_api import BaseAPI
from data.endpoints import Endpoints


class OrderAPI(BaseAPI):

    def create_order(self, order_data):
        """Создание заказа"""
        return self.post(Endpoints.ORDER_CREATE, order_data)

    def get_order_by_track(self, track_number):
        """Получение заказа по трекингу"""
        params = {"t": track_number}
        return self.get(Endpoints.ORDER_TRACK, params)

    def accept_order(self, order_id, courier_id):
        """Принять заказ"""
        endpoint = Endpoints.ORDER_ACCEPT.format(id=order_id)
        params = {"courierId": courier_id}
        return self.put(endpoint, params=params)

    def finish_order(self, order_id):
        """Завершить заказ"""
        endpoint = Endpoints.ORDER_FINISH.format(id=order_id)
        return self.put(endpoint, {"id": order_id})

    def cancel_order(self, track_number):
        """Отменить заказ"""
        return self.put(Endpoints.ORDER_CANCEL, {"track": track_number})

    def get_orders_list(self, courier_id=None, nearest_station=None, limit=30, page=0):
        """Получение списка заказов"""
        params = {
            "limit": limit,
            "page": page
        }

        if courier_id:
            params["courierId"] = courier_id

        if nearest_station:
            params["nearestStation"] = nearest_station

        return self.get(Endpoints.ORDER_LIST, params)

    def ping_server(self):
        """Проверка доступности сервера"""
        return self.get(Endpoints.PING)

    def search_stations(self, search_string):
        """Поиск станций метро"""
        params = {"s": search_string}
        return self.get(Endpoints.STATIONS_SEARCH, params)