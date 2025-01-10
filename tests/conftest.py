import pytest
from utils.cheking import Cheking
from utils.api import GoogleMapsApi

@pytest.fixture(scope="function")
def fixt():
    print("Метод POST")
    result_post = GoogleMapsApi.create_new_place()
    place_id = result_post.json()['place_id']
    Cheking.check_status_code(result_post, 200)
    Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
    Cheking.check_json_value(result_post, 'status', 'OK')
    return place_id
