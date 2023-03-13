from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from clients.users_client import UsersClient
from uuid import uuid4
from enums.user_role_enum import UserRoleEnum
from enums.ticket_status_enum import TicketStatusEnum
from controllers.tickets_controller import TicketsController
from services.tickets_service import TicketsService
from repositories.ticket_repository import TicketRepository

port = 8001
app = Flask(__name__)

CORS(app, resources={f"/api/*": { "origins": "*" }})

load_dotenv(find_dotenv())

TicketsController(app, TicketsService(TicketRepository()))

if __name__ == '__main__':
    app.run(debug=True, port=port)
