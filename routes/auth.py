from flask_expects_json import expects_json


from app.blueprint import auth, api_auth
from api import auth as auth_api
from views import auth as auth_views
from validators import USER_REGISTER_SCHEMA


@auth.route("/login", methods=["GET", "POST"])
def login():
    return auth_views.login()


@auth.route("/logout")
def logout():
    return auth_views.logout()


@api_auth.route("/user/create", methods=["POST"])
@expects_json(USER_REGISTER_SCHEMA)
def user_create():
    return auth_api.user_create()