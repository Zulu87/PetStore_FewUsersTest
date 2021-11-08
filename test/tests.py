from api_client.user_client import *



class TestUsers:

    # тест на додавання одного юзера
    def test_user_is_added(self, current_user_client: UserClient, users_data_provider):
        single_user_request = current_user_client.add_user(data_payload = users_data_provider("single_user_data.csv"))

        assert single_user_request.status_code == 200, f"Request failed with the status code {single_user_request.status_code}"

    # тест на додавання кількох юзерів списком
    def test_few_users_are_added(self, current_user_client: UserClient, users_data_provider):
        few_users_request = current_user_client.add_user(data_payload = users_data_provider("multiple_users_data.csv"), param="createWithList")

        assert few_users_request.status_code == 200, f"Request failed with the status code {few_users_request.status_code}"