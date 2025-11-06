import json


class Helpers:

    @staticmethod
    def extract_json(response):
        """Извлечение JSON из ответа"""
        try:
            return response.json()
        except json.JSONDecodeError:
            return {}

    @staticmethod
    def check_response_status(response, expected_status):
        """Проверка статуса ответа"""
        assert response.status_code == expected_status, \
            f"Expected status {expected_status}, but got {response.status_code}. " \
            f"Response: {response.text}"

    @staticmethod
    def check_error_message(response, expected_message):
        """Проверка сообщения об ошибке"""
        response_data = Helpers.extract_json(response)
        assert "message" in response_data, f"No error message in response. Response: {response_data}"
        assert response_data["message"] == expected_message, \
            f"Expected message '{expected_message}', but got '{response_data['message']}'"

    @staticmethod
    def check_field_exists(response, field_name):
        """Проверка наличия поля в ответе"""
        response_data = Helpers.extract_json(response)
        assert field_name in response_data, f"Field '{field_name}' not found in response: {response_data}"
        return response_data[field_name]