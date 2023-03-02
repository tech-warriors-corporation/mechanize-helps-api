import requests
from clients.client import Client

class UsersClient(Client):
    def __init__(self, api_url: str):
        super().__init__(api_url)

    def get_user(self, id: int):
        response = requests.get(f"{self._api_url}/{id}")

        return response.json()
