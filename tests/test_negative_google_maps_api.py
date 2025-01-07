from utils.api import GoogleMapsApi
from utils.cheking import Cheking
import allure

@allure.epic("Негативные кейсы ")
class TestNegative:
    """"Негативные тесты"""

    @allure.description("Изменение удаленной локации")
    def test_changing_a_removed_place(self):
        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Cheking.check_status_code(result_put, 404)
        Cheking.check_json_value(result_put, 'msg', "Update address operation failed,"
                                                    " looks like the data doesn't exists")

    @allure.description("Удаление несуществующей локации")
    def test_changing_a_non_existing_place(self):
        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place("random")
        Cheking.check_status_code(result_put, 404)
        Cheking.check_json_value(result_put, 'msg', "Update address operation failed,"
                                                    " looks like the data doesn't exists")

    @allure.description("Получение удаленной локации")
    def test_get_a_removed_place(self):
        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json()['place_id']
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id"
                                                    "  doesn't exists")  #Проверка всего текста
        Cheking.check_json_search_word_in_value(result_get,'msg','failed')                                          # Проверка слова или части текста

    @allure.description("Получение несуществующей локации")
    def test_delete_non_existent_place(self):

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place("random")
        Cheking.check_status_code(result_delete, 404)
        Cheking.check_json_value(result_delete, 'msg', "Delete operation failed, looks like the"
                                                       " data doesn't exists")

