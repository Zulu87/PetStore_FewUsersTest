import pytest
import csv
from api_client.user_client import UserClient


@pytest.fixture(scope="session")
def current_user_client(request):
    api_client = UserClient()
    yield api_client
    del api_client

#фікстура для передавання даних з csv файлу в пейлод реквеста
@pytest.fixture(scope="function")
def users_data_provider():
    def _csv_to_dict(a):
        with open(a, 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
            dict_reader = csv.DictReader(read_obj)
    # get a list of dictionaries from dct_reader
            list_of_dict = list(dict_reader)
    # go threw dictionaries and convert id's and userStatuses from string format to integer
            for i in range(len(list_of_dict)):
                for x in ('id','userStatus'):
                    list_of_dict[i][x] = int(list_of_dict[i][x])
            if len(list_of_dict)==1:
                return list_of_dict[0]
            else:
                return list_of_dict

    return _csv_to_dict