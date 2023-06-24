import requests
from clients.client import Client

class NominatimClient(Client):
    def __init__(self, api_url: str):
        super().__init__(api_url)

    def get_location(self, lat: str, lon: str):
        response = requests.get(f"{self._api_url}/reverse?format=json&lat={lat}&lon={lon}")

        return response.json()
