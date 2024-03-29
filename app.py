from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from controllers.tickets_controller import TicketsController
from services.tickets_service import TicketsService
from repositories.ticket_repository import TicketRepository
from clients.users_client import UsersClient
from os import environ

app = Flask(__name__)

CORS(app, resources={f"/api/*": { "origins": "*" }})

load_dotenv(find_dotenv())

TicketsController(app, TicketsService(TicketRepository()), UsersClient(environ.get("ACCOUNTS_API_URL")))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8001)
