from api_client.abstract_api_client import AbstractApiClient

#АПІ клієнт для колання ендпоїнта User
class UserClient(AbstractApiClient):
    user_endpoint = "user"

    def add_user(self, data_payload, param = None):
        return self._post(endpoint=UserClient.user_endpoint, payload = data_payload, param=param)