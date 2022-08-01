from datetime import datetime
from app.db import db


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
    from_ = db.Column("from", db.Integer, db.ForeignKey("auth_user.id"), nullable=False)
    to = db.Column("to", db.Integer, db.ForeignKey("auth_user.id"), nullable=False)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime)

    def __repr__(self) -> str:
        """
        Return a string representation of the message model.
        """

        return "<Message >" % self.text

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
            'from': self.from_,
            'to': self.to,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }