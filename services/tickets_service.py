from repositories.ticket_repository import TicketRepository
from enums.ticket_status_enum import TicketStatusEnum
from texts import sanitize

class TicketsService:
    def __init__(self, ticket_repository: TicketRepository):
        self.__ticket_repository = ticket_repository

    def create(self, driver_id: int, vehicle: str, location: str, description: str, status: TicketStatusEnum) -> int:
        if not driver_id:
            raise ValueError('Driver id is required')

        if not isinstance(driver_id, int):
            raise ValueError('Driver id should be integer')

        if not vehicle:
            raise ValueError('Vehicle is required')

        if not location:
            raise ValueError('Location is required')

        if not description:
            raise ValueError('Description is required')

        if not status:
            raise ValueError('Status is required')

        if status != TicketStatusEnum.UNSOLVED.value and status != TicketStatusEnum.SOLVED.value and status != TicketStatusEnum.CANCELLED.value:
            raise ValueError('Status is invalid')

        vehicle = sanitize(vehicle)
        description = sanitize(description)

        return self.__ticket_repository.create(driver_id, vehicle, location, description, status)

    def cancel_ticket(self, id: int, user_id: int, is_mechanic: bool) -> int:
        if not id:
            raise ValueError('Id is required')

        if not isinstance(id, int):
            raise ValueError('Id should be integer')

        if not user_id:
            raise ValueError('User id is required')

        if not isinstance(user_id, int):
            raise ValueError('User id should be integer')

        if not isinstance(is_mechanic, bool):
            raise ValueError('Is mechanic should be boolean')

        return self.__ticket_repository.cancel_ticket(id, user_id, is_mechanic)

    def accept_ticket(self, id: int, mechanic_id: int) -> int:
        if not id:
            raise ValueError('Id is required')

        if not isinstance(id, int):
            raise ValueError('Id should be integer')

        if not mechanic_id:
            raise ValueError('Mechanic id is required')

        if not isinstance(mechanic_id, int):
            raise ValueError('Mechanic id should be integer')

        return self.__ticket_repository.accept_ticket(id, mechanic_id)

    def conclude_ticket(self, id: int, user_id: int) -> int:
        if not id:
            raise ValueError('Id is required')

        if not isinstance(id, int):
            raise ValueError('Id should be integer')

        if not user_id:
            raise ValueError('User id is required')

        if not isinstance(user_id, int):
            raise ValueError('User id should be integer')

        return self.__ticket_repository.conclude_ticket(id, user_id)

    def get_available_tickets(self, token: str, client_id: str):
        return self.__ticket_repository.get_available_tickets(token, client_id)

    def get_ticket_status(self, token: str, client_id: str, id: int, user_id: int):
        if not token:
            raise ValueError('Token is required')

        if not isinstance(token, str):
            raise ValueError('Token should be string')

        if not client_id:
            raise ValueError('Client id is required')

        if not isinstance(client_id, str):
            raise ValueError('Client id should be string')

        if not id:
            raise ValueError('Id is required')

        if not isinstance(id, int):
            raise ValueError('Id should be integer')

        return self.__ticket_repository.get_ticket_status(token, client_id, id, user_id)

    def rating_ticket(self, id: int, driver_id: int, rating: int):
        if not id:
            raise ValueError('Id is required')

        if not isinstance(id, int):
            raise ValueError('Id should be integer')

        if not driver_id:
            raise ValueError('Driver id is required')

        if not isinstance(driver_id, int):
            raise ValueError('Driver id should be integer')

        if not rating:
            raise ValueError('Rating is required')

        if not isinstance(rating, int):
            raise ValueError('Rating should be integer')

        if rating < 1 or rating > 5:
            raise ValueError('Rating should be smaller or equal than 5 and bigger or equal than 1')

        return self.__ticket_repository.rating_ticket(id, driver_id, rating)

    def get_current_ticket(self, token: str, client_id: str, user_id: int):
        if not token:
            raise ValueError('Token is required')

        if not isinstance(token, str):
            raise ValueError('Token should be string')

        if not client_id:
            raise ValueError('Client id is required')

        if not isinstance(client_id, str):
            raise ValueError('Client id should be string')

        if not user_id:
            raise ValueError('User id is required')

        if not isinstance(user_id, int):
            raise ValueError('User id should be integer')

        return self.__ticket_repository.get_current_ticket(token, client_id, user_id)
