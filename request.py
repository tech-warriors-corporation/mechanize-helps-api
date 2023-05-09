from clients.users_client import UsersClient
from os import environ
from flask import request
from response import generate_response

users_client = UsersClient(environ.get("ACCOUNTS_API_URL"))

def should_be_logged(callback):
    def secure_function(*args, **kwargs):
        token = request.headers.get('Authorization')

        if token is None:
            return generate_response(status_code=401)

        is_valid_token: bool = users_client.has_valid_token(token)['payload']

        if is_valid_token is True:
            return callback(*args, **kwargs)
        else:
            return generate_response(status_code=401)

    secure_function.__name__ = callback.__name__

    return secure_function
