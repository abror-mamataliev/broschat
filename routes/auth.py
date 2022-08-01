from app.blueprint import auth
from views import auth as auth_views


@auth.route("/login", methods=["GET", "POST"])
def login():
    return auth_views.login()


@auth.route("/logout")
def logout():
    return auth_views.logout()
