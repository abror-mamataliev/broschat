from flask_socketio import (
    emit,
    join_room,
    leave_room,
    SocketIO,
)

from models import Message


def connect(socketio_app: SocketIO, chat: dict) -> None:
    """
    Handle the connect event.

    :param chat: The chat data.
    """

    room = chat['room']
    join_room(room)
    emit("status", {
        'message': f"You are connected to Room №{room}",
    }, room=room)


def send_message(socketio_app: SocketIO, message: dict) -> None:
    """
    Send a message to a chat.

    :param message: The message data.
    """

    room = message['room']
    msg = {
        'id': message['id'],
        'text': message['text'],
        'room': room,
    }
    message_instance = Message(**msg)
    message_instance.save()
    socketio_app.emit("message", message, room=room)


def disconnect(socketio_app: SocketIO, chat: dict) -> None:
    """
    Handle the disconnect event.

    :param chat: The chat data.
    """
    
    room = chat['room']
    leave_room(room)
