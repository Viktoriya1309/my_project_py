import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)

def post_new_client_kit():
    headers_with_auth = data.headers.copy()
    token = response.json()["authToken"]
    headers_with_auth["Authorization"] = f"Bearer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=data.kit_body,
                         headers=headers_with_auth)

response = post_new_client_kit()