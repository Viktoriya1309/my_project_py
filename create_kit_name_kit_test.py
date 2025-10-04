import configuration
import sender_stand_request
import data

sender_stand_request.post_new_user(data.user_body)

def kit_body(name):
    body = data.kit_body.copy()
    body["name"] = name
    return body

def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"

    response = sender_stand_request.post(configuration.CREATE_KIT_PATH, kit_body, headers_with_auth)

    assert response.status_code == 201, f"Ожидали 201, получили {response.status_code}: {response.text}"
    assert response.json().get("name") == kit_body["name"], "Имя набора не совпадает"

def negative_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"

    response = sender_stand_request.post(configuration.CREATE_KIT_PATH, kit_body, headers_with_auth)

    assert response.status_code == 400, f"Ожидали 400, получили {response.status_code}: {response.text}"

#1 test
def test_create_kit_with_name_length_1():
    test_kit_body = kit_body("a")  
    positive_assert(test_kit_body)

#2 test  
def test_create_kit_with_name_length_511():
    test_kit_body = kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC") 
    positive_assert(test_kit_body)

#3 test
def test_create_kit_with_name_length_0():
    test_kit_body = kit_body("") 
    negative_assert(test_kit_body)

#4 test
def test_create_kit_with_name_length_512():
    test_kit_body = kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD") 
    negative_assert(test_kit_body)

#5 test
def test_create_kit_with_name_english_letters():
    test_kit_body = kit_body("QWErty") 
    positive_assert(test_kit_body)

#6 test
def test_create_kit_with_name_russian_letters():
    test_kit_body = kit_body("Мария") 
    positive_assert(test_kit_body)

#7 test
def test_create_kit_with_name_with_simbols():
    test_kit_body = kit_body('"№%@",') 
    positive_assert(test_kit_body)

#8 test
def test_create_kit_with_name_with_space():
    test_kit_body = kit_body(" Человек и КО ") 
    positive_assert(test_kit_body)

#9 test
def test_create_kit_with_name_with_numbers():
    test_kit_body = kit_body("123") 
    positive_assert(test_kit_body)

#10 test
def test_create_kit_with_name_no_param():
    negative_assert({})

#11 test
def test_create_kit_with_name_another_param():
    test_kit_body = kit_body(123) 
    negative_assert(test_kit_body)