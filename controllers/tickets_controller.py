from services.tickets_service import TicketsService
from response import generate_response
from controllers.controller import Controller
from flask import Flask, request
from request import should_be_logged, should_be_valid_client_id, should_be_driver

class TicketsController(Controller):
    def __init__(self, app: Flask, tickets_service: TicketsService):
        super().__init__(app)

        self.__tickets_service = tickets_service

    def register_routes(self):
        self._app.add_url_rule('/api/helps/tickets', 'create', self.create, methods=['POST'])
        self._app.add_url_rule('/api/helps/tickets/<int:id>/cancel-ticket', 'cancel_ticket', self.cancel_ticket, methods=['PATCH'])

    @should_be_valid_client_id
    @should_be_logged
    @should_be_driver
    def create(self):
        try:
            data = request.get_json()
            id = self.__tickets_service.create(int(data['driver_id']), data['vehicle'], data['location'], data['description'], data['status'])

            return generate_response(id, 201)
        except Exception as error:
            return generate_response(str(error), 400)

    @should_be_valid_client_id
    @should_be_logged
    def cancel_ticket(self, id: int):
        try:
            result = self.__tickets_service.cancel_ticket(id)

            return generate_response(result, 200)
        except Exception as error:
            return generate_response(str(error), 400)
