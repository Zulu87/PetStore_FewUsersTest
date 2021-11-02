import requests
from api_client.helper import config_setter

base_url = config_setter("settings.yaml")["url"]
api_key = config_setter("settings.yaml")["api_key"]


class AbstractApiClient:
    def __init__(self):
        self.__api_key = api_key
        self.__client = requests.Session()

    #пропертя додає до недерів апі-ключ який бере з файла сеттінгс
    @property
    def headers_with_api(self):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        headers.update({"api_key": api_key})
        return headers

    # оголошуємо метод який виконуватиме get запити
    def _get(self, endpoint, param):
        url = f"{base_url}/{endpoint}/{param}"
        res = self.__client.get(url, headers = self.headers_with_api)
        return res

    # оголошуємо метод який виконуватиме delete запити
    def _delete(self, endpoint, param):
        url = f"{base_url}/{endpoint}/{param}"
        res = self.__client.delete(url, headers = self.headers_with_api)
        return res

    # оголошуємо метод який виконуватиме post запити
    def _post(self, endpoint, payload, param = None ):
        if param:
            url = f"{base_url}/{endpoint}/{param}"
        else:
            url = f"{base_url}/{endpoint}"
        res = self.__client.post(url, headers = self.headers_with_api, json = payload)
        return res

    # оголошуємо метод який виконуватиме put запити
    def _put(self, endpoint, payload, param = None ):
        if param:
            url = f"{base_url}/{endpoint}/{param}"
        else:
            url = f"{base_url}/{endpoint}"
        res = self.__client.put(url, headers = self.headers_with_api, json = payload)
        return res

    def __del__(self):
        self.__client.close()
