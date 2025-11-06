from api.base_api import BaseAPI
from data.endpoints import Endpoints


class CourierAPI(BaseAPI):

    def create_courier(self, login, password, first_name):
        """Создание курьера"""
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return self.post(Endpoints.COURIER_CREATE, data)

    def login_courier(self, login, password):
        """Логин курьера"""
        data = {
            "login": login,
            "password": password
        }
        return self.post(Endpoints.COURIER_LOGIN, data)

    def delete_courier(self, courier_id):
        """Удаление курьера"""
        endpoint = Endpoints.COURIER_DELETE.format(id=courier_id)
        return self.delete(endpoint, {"id": str(courier_id)})

    def get_orders_count(self, courier_id):
        """Получение количества заказов курьера"""
        endpoint = Endpoints.COURIER_ORDERS_COUNT.format(id=courier_id)
        return self.get(endpoint)