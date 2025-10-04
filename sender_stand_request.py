import configuration
import requests
import data

def post(path, body, headers):
    return requests.post(configuration.URL_SERVICE + path, json=body, headers=headers)

def post_new_user(body):
    return post(configuration.CREATE_USER_PATH, body, data.headers)

def get_new_user_token():
    response = post(configuration.CREATE_USER_PATH, data.user_body, data.headers)
    return response.json().get("authToken")