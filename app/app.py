from flask import Flask
from flask_socketio import SocketIO
from os.path import dirname
from typing import Tuple

from app.blueprint import register_blueprints
from app.db import (
    migrate_db,
    register_db
)
from app.login_manager import register_login_manager
from routes import *
from utils import (
    get_config,
)


def create_app(type: str = "dev") -> Tuple[Flask, SocketIO]:
    """
    Create a Flask application and a SocketIO instance.
    
    :param type: The type of the application.
    :return: A tuple of the Flask application and the SocketIO instance.
    """

    app: Flask = Flask(dirname(dirname(__file__)))
    config: str = get_config(type)
    app.config.from_pyfile(f"config/{config}.py")
    register_blueprints(app)
    register_db(app)
    register_login_manager(app)
    if app.config.get('DEBUG'):
        migrate_db(app)
    socketio_app: SocketIO = SocketIO(app, manage_session=False)

    return app, socketio_app
