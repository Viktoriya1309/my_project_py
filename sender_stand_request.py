import configuration
import requests
import data

def create_new_kit(body, headers):
    return requests.post(configuration.CREATE_KIT_PATH, json=body, headers=headers)

def create_user_and_retrieve_token():
    response = requests.post(configuration.CREATE_USER_PATH, json=data.user_body, headers=data.headers)
    return response.json().get("authToken")