from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
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
