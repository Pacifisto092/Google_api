from utils.api import GoogleMapsApi
from utils.cheking import Cheking
from utils.json import *
import allure

@allure.epic("Позитивные кейсы ")
class TestPositive:
    """"Позитивные тесты: Создание, изменение и удаление локации"""

    @allure.description("Создание и получение локации")
    def test_create_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                              'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'address', json_for_create_new_place['address'])

    @allure.description("Обновление локации")
    def test_update_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                              'types', 'website', 'language'])
        Cheking.check_json_value(result_get, 'address', json_for_update_place['address'])

    @allure.description("Удаление локации")
    def test_delete_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', 'OK')
