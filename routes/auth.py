from app.blueprint import (
    auth,
    api_auth
)
from api import auth as auth_api
from views import auth as auth_views


@auth.route("/login", methods=["GET", "POST"])
def login():
    return auth_views.login()


@auth.route("/logout")
def logout():
    return auth_views.logout()


@api_auth.route("/user/create", methods=["POST"])
def user_create():
    return auth_api.user_create()