import requests
from data.endpoints import Endpoints


class BaseAPI:
    def __init__(self):
        self.base_url = Endpoints.BASE_URL
        self.headers = {
            'Content-Type': 'application/json'
        }

    def post(self, endpoint, json_data=None):
        url = self.base_url + endpoint
        return requests.post(url, json=json_data, headers=self.headers)

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        return requests.get(url, params=params, headers=self.headers)

    def put(self, endpoint, json_data=None, params=None):
        url = self.base_url + endpoint
        return requests.put(url, json=json_data, params=params, headers=self.headers)

    def delete(self, endpoint, json_data=None):
        url = self.base_url + endpoint
        return requests.delete(url, json=json_data, headers=self.headers)