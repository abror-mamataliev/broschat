from flask_socketio import SocketIO

from views import socket as socket_views


def register_socketio_events(socketio_app: SocketIO) -> None:
    """
    Register the SocketIO events.
    
    :param socketio_app: The SocketIO application.
    """

    @socketio_app.on("join", namespace="/chat")
    def connect(chat: dict) -> None:
        """
        Handle the connect event.
        
        :param chat: The chat data.
        """

        socket_views.connect(chat)
    
    @socketio_app.on("leave", namespace="/chat")
    def disconnect(chat: dict) -> None:
        """
        Handle the disconnect event.
        
        :param chat: The chat data.
        """

        socket_views.disconnect(chat)
