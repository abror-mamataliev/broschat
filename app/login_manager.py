from flask import (
    Flask,
    redirect,
    url_for
)
from flask_login import LoginManager

from models import User


login_manager: LoginManager = LoginManager()


def register_login_manager(app: Flask) -> None:
    """
    Register the login manager to the Flask application.

    :param app: The Flask application.
    """

    @login_manager.user_loader
    def load_user(id):
        return User.get_by_id(id)

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return redirect(url_for("auth.login"))
    
    login_manager.init_app(app)
