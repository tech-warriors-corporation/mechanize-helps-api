from repositories.ticket_repository import TicketRepository
from enums.ticket_status_enum import TicketStatusEnum

class TicketsService:
    def __init__(self, ticket_repository: TicketRepository):
        self.__ticket_repository = ticket_repository

    def create(self, driver_id: int, mechanic_id: int, vehicle: str, location: str, description: str, status: TicketStatusEnum) -> int:
        if not driver_id:
            raise ValueError('Driver id is required')

        if not isinstance(driver_id, int):
            raise ValueError('Driver id should be integer')

        if not mechanic_id:
            raise ValueError('Mechanic id is required')

        if not isinstance(mechanic_id, int):
            raise ValueError('Mechanic id should be integer')

        if not vehicle:
            raise ValueError('Vehicle is required')

        if not location:
            raise ValueError('Location is required')

        if not description:
            raise ValueError('Description is required')

        if not status:
            raise ValueError('Status is required')

        if status != TicketStatusEnum.ATTENDING.value and status != TicketStatusEnum.SOLVED.value:
            raise ValueError('Status is invalid')

        return self.__ticket_repository.create(driver_id, mechanic_id, vehicle, location, description, status)
