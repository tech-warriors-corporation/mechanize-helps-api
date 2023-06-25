from clients.users_client import UsersClient
from clients.nominatim_client import NominatimClient
from os import environ
from entities.entity import Entity
import datetime

class TicketEntity(Entity):
    def __init__(self):
        super().__init__()

        self.__users_client = UsersClient(environ.get("ACCOUNTS_API_URL"))
        self.__nominatim_client = NominatimClient(environ.get("NOMINATIM_API_URL"))
        self.__google_maps_url = environ.get("GOOGLE_MAPS_URL")

    def generate_entity(self, token: str, client_id: str, id: int, driver_id: int, vehicle: str, lat: str, lon: str, description: str, created_date: datetime.datetime):
        try:
            return {
                'id': id,
                'driver_name': self.__users_client.get_user_name_by_id(token, client_id, driver_id)['payload'],
                'vehicle': vehicle,
                'location': self.__nominatim_client.get_location(lat, lon)['display_name'],
                'lat': lat,
                'lon': lon,
                'google_maps_link': f'{self.__google_maps_url}/search/{lat},{lon}/@{lat},{lon},15z?entry=ttu',
                'description': description,
                'created_date': created_date.strftime("%d/%m/%Y (%H:%M)"),
            }
        except Exception as error:
            print(error)
            return None
