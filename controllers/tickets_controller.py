from services.tickets_service import TicketsService
from response import generate_response
from controllers.controller import Controller
from flask import Flask, request
from request import should_be_logged, should_be_valid_client_id, should_be_driver, should_be_mechanic
from clients.users_client import UsersClient

class TicketsController(Controller):
    def __init__(self, app: Flask, tickets_service: TicketsService, users_client: UsersClient):
        super().__init__(app)

        self.__tickets_service = tickets_service
        self.__users_client = users_client

    def register_routes(self):
        self._app.add_url_rule('/api/helps/tickets', 'create', self.create, methods=['POST'])
        self._app.add_url_rule('/api/helps/tickets/<int:id>/cancel-ticket', 'cancel_ticket', self.cancel_ticket, methods=['PATCH'])
        self._app.add_url_rule('/api/helps/tickets/<int:id>/accept-ticket', 'accept_ticket', self.accept_ticket, methods=['PATCH'])
        self._app.add_url_rule('/api/helps/tickets/<int:id>/conclude-ticket', 'conclude_ticket', self.conclude_ticket, methods=['PATCH'])
        self._app.add_url_rule('/api/helps/tickets/<int:id>/rating', 'rating_ticket', self.rating_ticket, methods=['PATCH'])
        self._app.add_url_rule('/api/helps/tickets/<int:id>/status', 'get_ticket_status', self.get_ticket_status, methods=['GET'])
        self._app.add_url_rule('/api/helps/tickets/available', 'get_available_tickets', self.get_available_tickets, methods=['GET'])
        self._app.add_url_rule('/api/helps/tickets/current-ticket', 'get_current_ticket', self.get_current_ticket, methods=['GET'])

    @should_be_valid_client_id
    @should_be_logged
    @should_be_driver
    def create(self):
        try:
            data = request.get_json()
            id = self.__tickets_service.create(int(data['driver_id']), data['vehicle'], data['location'], data['description'], data['status'])

            return generate_response(id, 201)
        except Exception as error:
            print(error)
            return generate_response(status_code=400)

    @should_be_valid_client_id
    @should_be_logged
    def cancel_ticket(self, id: int):
        try:
            token = request.headers.get('Authorization')
            client_id = request.headers.get('clientId')
            user_id = self.__users_client.get_id_by_token(token, client_id)['payload']
            is_mechanic = self.__users_client.is_mechanic(token, client_id)['payload']
            result = self.__tickets_service.cancel_ticket(id, user_id, is_mechanic)

            return generate_response(result, 200)
        except Exception as error:
            print(error)
            return generate_response(status_code=400)

    @should_be_valid_client_id
    @should_be_logged
    @should_be_mechanic
    def accept_ticket(self, id: int):
        try:
            token = request.headers.get('Authorization')
            client_id = request.headers.get('clientId')
            mechanic_id = self.__users_client.get_id_by_token(token, client_id)['payload']

            return generate_response(self.__tickets_service.accept_ticket(id, mechanic_id), 200)
        except Exception as error:
            print(error)
            return generate_response(status_code=400)

    @should_be_valid_client_id
    @should_be_logged
    def conclude_ticket(self, id: int):
        try:
            token = request.headers.get('Authorization')
            client_id = request.headers.get('clientId')
            user_id = self.__users_client.get_id_by_token(token, client_id)['payload']

            return generate_response(self.__tickets_service.conclude_ticket(id, user_id), 200)
        except Exception as error:
            print(error)
            return generate_response(status_code=400)

    @should_be_valid_client_id
    @should_be_logged
    @should_be_mechanic
    def get_available_tickets(self):
        try:
            token = request.headers.get('Authorization')
            client_id = request.headers.get('clientId')

            return generate_response(self.__tickets_service.get_available_tickets(token, client_id), 200)
        except Exception as error:
            print(error)
            return generate_response([], status_code=400)

    @should_be_valid_client_id
    @should_be_logged
    def get_ticket_status(self, id: int):
        try:
            return generate_response(self.__tickets_service.get_ticket_status(id), 200)
        except Exception as error:
            print(error)
            return generate_response(status_code=400)

    @should_be_valid_client_id
    @should_be_logged
    @should_be_driver
    def rating_ticket(self, id: int):
        try:
            data = request.get_json()
            token = request.headers.get('Authorization')
            client_id = request.headers.get('clientId')
            driver_id = self.__users_client.get_id_by_token(token, client_id)['payload']

            return generate_response(self.__tickets_service.rating_ticket(id, driver_id, int(data['rating'])), 200)
        except Exception as error:
            print(error)
            return generate_response(status_code=400)

    @should_be_valid_client_id
    @should_be_logged
    def get_current_ticket(self):
        try:
            token = request.headers.get('Authorization')
            client_id = request.headers.get('clientId')
            user_id = self.__users_client.get_id_by_token(token, client_id)['payload']

            return generate_response(self.__tickets_service.get_current_ticket(token, client_id, user_id), 200)
        except Exception as error:
            print(error)
            return generate_response(status_code=400)
