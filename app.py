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

users_client = UsersClient('http://localhost:8000/api/accounts/users')
driver_id = users_client.create('João (driver)', f'joao-{uuid4()}@driver.com', 'JoaoDriver1234', UserRoleEnum.DRIVER.value)['payload']
mechanic_id = users_client.create('João (mechanic)', f'joao-{uuid4()}@mechanic.com', 'JoaoMechanic1234', UserRoleEnum.MECHANIC.value)['payload']
driver = users_client.get(driver_id)['payload']
mechanic = users_client.get(mechanic_id)['payload']
client = app.test_client()

ticket_id = client.post(f"http://localhost:{port}/api/helps/tickets", json={
    'driver_id': driver['id'],
    'mechanic_id': mechanic['id'],
    'vehicle': 'Mercedes-Benz CLS53 AMG 3.0',
    'location': 'São Paulo, Brazil',
    'description': f'Envolved users emails are: {driver["email"]} and {mechanic["email"]}',
    'status': TicketStatusEnum.ATTENDING.value,
}).json['payload']

print(f"Created ticket with id: {ticket_id}")

if __name__ == '__main__':
    app.run(debug=True, port=port)
