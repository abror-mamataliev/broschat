from flask import Flask
from flask_socketio import SocketIO
from os.path import dirname
from typing import Tuple

from app.blueprint import register_blueprints
from app.db import migrate_db, register_db

from routes import *


def create_app(type: str = "dev") -> Tuple[Flask, SocketIO]:
    """
    Create a Flask application and a SocketIO instance.
    
    :param type: The type of the application.
    :return: A tuple of the Flask application and the SocketIO instance.
    """

    app: Flask = Flask(dirname(dirname(__file__)))

    if type == "dev":
        app.config.from_pyfile("config/dev.py")
    elif type == "test":
        app.config.from_pyfile("config/test.py")
    else:
        app.config.from_pyfile("config/prod.py")
    
    register_blueprints(app)
    register_db(app)
    if app.config.get('DEBUG'):
        migrate_db(app)

    socketio_app: SocketIO = SocketIO(app, manage_session=False)

    return app, socketio_app
