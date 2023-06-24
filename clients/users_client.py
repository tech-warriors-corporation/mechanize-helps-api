import requests
from clients.client import Client

class UsersClient(Client):
    def __init__(self, api_url: str):
        super().__init__(api_url)

    def has_valid_token(self, token: str, client_id: str):
        response = requests.get(f"{self._api_url}/has-valid-token", headers={ "Authorization": token, "clientId": client_id })

        return response.json()

    def is_driver(self, token: str, client_id: str):
        response = requests.get(f"{self._api_url}/is-driver", headers={ "Authorization": token, "clientId": client_id })

        return response.json()

    def is_mechanic(self, token: str, client_id: str):
        response = requests.get(f"{self._api_url}/is-mechanic", headers={ "Authorization": token, "clientId": client_id })

        return response.json()

    def get_user_name_by_id(self, token: str, client_id: str, id: int):
        response = requests.get(f"{self._api_url}/users/{id}/user-name", headers={ "Authorization": token, "clientId": client_id })

        return response.json()

    def get_id_by_token(self, token: str, client_id: str):
        response = requests.get(f"{self._api_url}/get-id-by-token", headers={ "Authorization": token, "clientId": client_id })

        return response.json()
