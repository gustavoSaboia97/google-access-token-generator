from flask import Flask

from src.routes.google_routes import google_blueprint

app = Flask(__name__)

app.register_blueprint(google_blueprint)
