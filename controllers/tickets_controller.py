from services.tickets_service import TicketsService
from response import generate_response
from controllers.controller import Controller
from flask import Flask, request

class TicketsController(Controller):
    def __init__(self, app: Flask, tickets_service: TicketsService):
        super().__init__(app)

        self.__tickets_service = tickets_service

    def register_routes(self):
        self._app.add_url_rule('/api/helps/tickets', 'create', self.create, methods=['POST'])

    def create(self):
        try:
            data = request.get_json()
            id = self.__tickets_service.create(data['driver_id'], data['mechanic_id'], data['vehicle'], data['location'], data['description'], data['status'])

            return generate_response(id, 201)
        except Exception as error:
            return generate_response(str(error), 400)
