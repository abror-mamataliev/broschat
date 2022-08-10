from datetime import datetime

from app.db import db
from models import User


class Room(db.Model):

    __tablename__ = "chat_room"

    id = db.Column(db.Integer, primary_key=True)
    user_1 = db.Column(db.Integer, db.ForeignKey("auth_user.id"))
    user_2 = db.Column(db.Integer, db.ForeignKey("auth_user.id"))

    messages = db.relationship("Message", backref="room", lazy=True)

    def __repr__(self) -> str:
        """
        Return a string representation of the room model.
        """

        user_1 = db.session.query(User.username).filter_by(id=self.user_1).first()[0]
        user_2 = db.session.query(User.username).filter_by(id=self.user_2).first()[0]
        return f"<Room ({user_1} - {user_2})>"
    
    def __str__(self) -> str:
        """
        Return a string representation of the room model.
        """

        user_1 = db.session.query(User.username).filter_by(id=self.user_1).first()[0]
        user_2 = db.session.query(User.username).filter_by(id=self.user_2).first()[0]
        return f"{user_1} - {user_2}"

    def save(self) -> None:
        """
        Save the room model.
        """

        db.session.add(self)
        db.session.commit()


class Message(db.Model):
    """
    Message model.
    
    Attributes:
        id: The id of the message.
        text: The text of the message.
        from: The sender of the message.
        to: The receiver of the message.
        created_at: The created time of the message.
        updated_at: The updated time of the message.
    """

    __tablename__ = "chat_message"

    id = db.Column("id", db.Integer, primary_key=True)
    text = db.Column("text", db.String(255))
    room_id = db.Column(db.Integer, db.ForeignKey("chat_room.id"))
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())

    def __repr__(self) -> str:
        """
        Return a string representation of the message model.
        """

        return f"<Message {self.text}>"

    def __str__(self) -> str:
        """
        Return a string representation of the message model.
        """

        return self.text

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the message model.
        """

        return {
            'id': self.id,
            'text': self.text,
            'room': self.room,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def save(self) -> None:
        """
        Save the message model.
        """

        db.session.add(self)
        db.session.commit()
