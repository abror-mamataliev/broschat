from flask import Blueprint, Flask


auth: Blueprint = Blueprint("auth", __name__, url_prefix="/auth")
chat: Blueprint = Blueprint("chat", __name__)


def register_blueprints(app: Flask) -> None:
    """
    Register the blueprints to the Flask application.

    :param app: The Flask application.
    """

    app.register_blueprint(auth)
    app.register_blueprint(chat)
