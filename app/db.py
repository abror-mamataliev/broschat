from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()


from models import *


def register_db(app: Flask) -> None:
    """
    Register the database to the Flask application.

    :param app: The Flask application.
    """

    db.init_app(app)


def migrate_db(app: Flask) -> None:
    """
    Migrate the database to the latest version.

    :param app: The Flask application.
    """

    with app.app_context():
        db.create_all()
