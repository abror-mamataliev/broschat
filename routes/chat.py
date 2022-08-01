from app.blueprint import chat
from views import chat as chat_views


@chat.route("/")
def index():
    return chat_views.index()
