from abc import ABC

class Client(ABC):
    def __init__(self, api_url: str):
        self._api_url = api_url
