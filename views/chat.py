from flask import render_template
from flask_login import current_user

from models import User, Room


def index():
    users = []
    for user in User.get_all():
        if user.id != current_user.id:
            users.append(user.to_dict())
    return render_template("chat/index.html", users=users)


def chat_view(username):
    user = User.get_by_username(username)
    room = Room.query.filter(
        Room.user_1 == current_user.id,
        Room.user_2 == user.id
    ).first()
    return render_template("chat/user.html", user=user, room=room.id)
