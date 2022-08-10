from flask import (
    redirect,
    render_template,
    request,
    url_for
)
from flask_login import (
    login_user,
    logout_user
)

from forms import LoginForm


def login():
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            user = form.get_user()
            login_user(user)
            return redirect(url_for("chat.index"))
    else:
        form = LoginForm()
        return render_template("auth/login.html", form=form)


def logout():
    logout_user()
    return redirect(url_for("auth.login"))
