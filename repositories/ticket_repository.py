from database import get_connection
from enums.ticket_status_enum import TicketStatusEnum

class TicketRepository:
    def __init__(self):
        self.__connection = None

    def create(self, driver_id: int, vehicle: str, location: str, description: str, status: str) -> int:
        self.__connection = get_connection()
        cursor = self.__connection.cursor()

        cursor.execute(f"INSERT INTO tickets (driver_id, vehicle, location, description, status) VALUES ({driver_id}, '{vehicle}', '{location}', '{description}', '{status}') RETURNING id")

        response = cursor.fetchone()
        id = response[0]

        self.__connection.commit()
        cursor.close()
        self.__connection.close()

        return id

    def cancel_ticket(self, id: int):
        self.__connection = get_connection()
        cursor = self.__connection.cursor()

        cursor.execute("UPDATE tickets SET status = %s WHERE id = %s", (TicketStatusEnum.CANCELLED.value, id))

        self.__connection.commit()
        cursor.close()
        self.__connection.close()

        return id
