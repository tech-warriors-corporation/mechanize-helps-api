from database import get_connection
from enums.ticket_status_enum import TicketStatusEnum
from entities.ticket_entity import TicketEntity

class TicketRepository:
    def __init__(self):
        self.__connection = None
        self.__ticket_entity = TicketEntity()

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

    def cancel_ticket(self, id: int, user_id: int) -> int:
        self.__connection = get_connection()
        cursor = self.__connection.cursor()

        cursor.execute(
            "UPDATE tickets SET status = %s WHERE id = %s AND (driver_id = %s OR mechanic_id = %s)",
            (TicketStatusEnum.CANCELLED.value, id, user_id, user_id)
        )

        self.__connection.commit()
        cursor.close()
        self.__connection.close()

        return id

    def accept_ticket(self, id: int, mechanic_id: int) -> int:
        self.__connection = get_connection()
        cursor = self.__connection.cursor()

        cursor.execute("UPDATE tickets SET mechanic_id = %s WHERE id = %s", (mechanic_id, id))

        self.__connection.commit()
        cursor.close()
        self.__connection.close()

        return id

    def conclude_ticket(self, id: int, user_id: int) -> int:
        self.__connection = get_connection()
        cursor = self.__connection.cursor()

        cursor.execute(
            "UPDATE tickets SET status = %s WHERE id = %s AND (driver_id = %s OR mechanic_id = %s)",
            (TicketStatusEnum.SOLVED.value, id, user_id, user_id)
        )

        self.__connection.commit()
        cursor.close()
        self.__connection.close()

        return id

    def get_available_tickets(self, token: str, client_id: str):
        self.__connection = get_connection()
        cursor = self.__connection.cursor()
        list = []

        cursor.execute(
            "SELECT id, driver_id, vehicle, location, description, created_date FROM tickets WHERE status = %s AND mechanic_id IS %s AND created_date >= CURRENT_TIMESTAMP - interval %s ORDER BY created_date DESC",
            (TicketStatusEnum.UNSOLVED.value, None, '24 hours')
        )

        data = cursor.fetchall()

        for item in data:
            location = item[3].split(',')
            ticket = self.__ticket_entity.generate_entity(token, client_id, item[0], item[1], item[2], location[0], location[1], item[4], item[5])

            if ticket is not None:
                list.append(ticket)

        cursor.close()
        self.__connection.close()

        return list

    def get_ticket_status(self, id: int):
        self.__connection = get_connection()
        cursor = self.__connection.cursor()

        cursor.execute(f"SELECT status, mechanic_id FROM tickets WHERE id = {id}")

        result = cursor.fetchone()
        ticket = { 'status': result[0], 'mechanic_id': result[1] }

        cursor.close()
        self.__connection.close()

        return ticket

    def rating_ticket(self, id: int, driver_id: int, rating: int) -> int:
        self.__connection = get_connection()
        cursor = self.__connection.cursor()

        cursor.execute("UPDATE tickets SET rating = %s WHERE id = %s AND driver_id = %s", (rating, id, driver_id))

        self.__connection.commit()
        cursor.close()
        self.__connection.close()

        return id

    def get_current_ticket(self, token: str, client_id: str, user_id: int):
        self.__connection = get_connection()
        cursor = self.__connection.cursor()
        unsolved_value = TicketStatusEnum.UNSOLVED.value

        cursor.execute(
            "SELECT id, driver_id, vehicle, location, description, created_date, mechanic_id, status "
            "FROM tickets "
            "WHERE (status = %s AND (driver_id = %s OR mechanic_id = %s)) OR "
            "(status <> %s AND driver_id = %s AND mechanic_id IS NOT NULL AND rating IS NULL)",
            (unsolved_value, user_id, user_id, unsolved_value, user_id)
        )

        item = cursor.fetchone()

        if item is None:
            return item

        id = item[0]
        mechanic_id = item[6]

        if mechanic_id is None:
            ticket_id = self.cancel_ticket(id, user_id)

            if not isinstance(ticket_id, int):
                raise ValueError('Ticket id should be integer')

            return None

        location = item[3].split(',')
        ticket = self.__ticket_entity.generate_entity(token, client_id, id, item[1], item[2], location[0], location[1], item[4], item[5])
        ticket['mechanic_id'] = mechanic_id
        ticket['status'] = item[7]

        cursor.close()
        self.__connection.close()

        return ticket
