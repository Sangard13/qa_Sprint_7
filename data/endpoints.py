class Endpoints:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    # Courier endpoints
    COURIER_CREATE = "/api/v1/courier"
    COURIER_LOGIN = "/api/v1/courier/login"
    COURIER_DELETE = "/api/v1/courier/{id}"
    COURIER_ORDERS_COUNT = "/api/v1/courier/{id}/ordersCount"

    # Order endpoints
    ORDER_CREATE = "/api/v1/orders"
    ORDER_TRACK = "/api/v1/orders/track"
    ORDER_ACCEPT = "/api/v1/orders/accept/{id}"
    ORDER_FINISH = "/api/v1/orders/finish/{id}"
    ORDER_CANCEL = "/api/v1/orders/cancel"
    ORDER_LIST = "/api/v1/orders"

    # Utils endpoints
    PING = "/api/v1/ping"
    STATIONS_SEARCH = "/api/v1/stations/search"