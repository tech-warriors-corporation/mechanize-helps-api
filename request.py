from clients.users_client import UsersClient
from os import environ
from flask import request
from response import generate_response

users_client = UsersClient(environ.get("ACCOUNTS_API_URL"))
valid_client_id = environ.get('CLIENT_ID')

def should_be_driver(callback):
    def secure_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        client_id = request.headers.get('clientId')

        if token is None:
            return generate_response(status_code=401)

        if users_client.is_driver(token, client_id)['payload'] is True:
            return callback(*args, **kwargs)

        return generate_response(status_code=401)

    secure_function.__name__ = callback.__name__

    return secure_function

def should_be_mechanic(callback):
    def secure_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        client_id = request.headers.get('clientId')

        if token is None:
            return generate_response(status_code=401)

        if users_client.is_mechanic(token, client_id)['payload'] is True:
            return callback(*args, **kwargs)

        return generate_response(status_code=401)

    secure_function.__name__ = callback.__name__

    return secure_function

def should_be_logged(callback):
    def secure_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        client_id = request.headers.get('clientId')

        if token is None:
            return generate_response(status_code=401)

        is_valid_token: bool = users_client.has_valid_token(token, client_id)['payload']

        if is_valid_token is True:
            return callback(*args, **kwargs)
        else:
            return generate_response(status_code=401)

    secure_function.__name__ = callback.__name__

    return secure_function

def should_be_valid_client_id(callback):
    def secure_function(*args, **kwargs):
        client_id = request.headers.get('clientId')

        if client_id == valid_client_id:
            return callback(*args, **kwargs)
        else:
            return generate_response(status_code=401)

    secure_function.__name__ = callback.__name__

    return secure_function
