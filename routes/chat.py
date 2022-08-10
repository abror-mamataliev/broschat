from flask_login import login_required

from app.blueprint import chat
from views import chat as chat_views


@chat.route("/")
@login_required
def index():
    return chat_views.index()


@chat.route("/<username>")
@login_required
def chat(username):
    return chat_views.chat_view(username)
