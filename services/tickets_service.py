from repositories.ticket_repository import TicketRepository
from enums.ticket_status_enum import TicketStatusEnum

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

        return self.__ticket_repository.create(driver_id, vehicle, location, description, status)

    def cancel_ticket(self, id: int) -> int:
        if not id:
            raise ValueError('Id is required')

        if not isinstance(id, int):
            raise ValueError('Id should be integer')

        return self.__ticket_repository.cancel_ticket(id)
