import requests
from clients.client import Client
from enums.user_role_enum import UserRoleEnum

class UsersClient(Client):
    def __init__(self, api_url: str):
        super().__init__(api_url)

    def create(self, name: str, email: str, password: str, role: UserRoleEnum):
        response = requests.post(f"{self._api_url}/users", json={ 'name': name, 'email': email, 'password': password, 'role': role })

        return response.json()

    def has_valid_token(self, token: str):
        response = requests.get(f"{self._api_url}/has-valid-token", headers={ "Authorization": token })

        return response.json()

    def get(self, id: int):
        response = requests.get(f"{self._api_url}/users/{id}")

        return response.json()
