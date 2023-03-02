from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from clients.users_client import UsersClient

app = Flask(__name__)

CORS(app, resources={f"/api/*": { "origins": "*" }})

load_dotenv(find_dotenv())

users_client = UsersClient('http://localhost:8000/api/accounts/users')

print(users_client.get_user(1))

if __name__ == '__main__':
    app.run(debug=True, port=8001)
