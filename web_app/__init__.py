# this is the "web_app/__init__.py" file...
import os

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.unemployment_routes import unemployment_routes
from web_app.routes.stocks_routes import stocks_routes


SECRET_KEY = os.getenv("SECRET_KEY", default="1234") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(unemployment_routes)
    app.register_blueprint(stocks_routes)