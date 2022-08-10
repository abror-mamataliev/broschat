from flask import (
    Blueprint,
    Flask
)


auth: Blueprint = Blueprint("auth", __name__, url_prefix="/auth")
api: Blueprint = Blueprint("api", __name__, url_prefix="/api")
chat: Blueprint = Blueprint("chat", __name__)

api_auth: Blueprint = Blueprint("api_auth", __name__, url_prefix="/auth")


def register_blueprints(app: Flask) -> None:
    """
    Register the blueprints to the Flask application.

    :param app: The Flask application.
    """

    register_api_blueprints(api)
    
    app.register_blueprint(auth)
    app.register_blueprint(api)
    app.register_blueprint(chat)


def register_api_blueprints(api: Blueprint) -> None:
    """
    Register the blueprints to the API blueprint.

    :param api: The API blueprint.
    """

    api.register_blueprint(api_auth)
