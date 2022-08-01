from datetime import datetime
from app.db import db


class User(db.Model):
    """
    User model.

    Attributes:
        id: The id of the user.
        first_name: The first name of the user.
        last_name: The last name of the user.
        username: The username of the user.
        password: The password of the user.
        photo: The photo of the user.
        phone_number: The phone number of the user.
        email: The email of the user.
        is_active: Activeness of the user.
        created_at: The created time of the user.
        last_login: The last login time of the user.
    """

    __tablename__ = "auth_user"

    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(255))
    last_name = db.Column("last_name", db.String(255))
    username = db.Column("username", db.String(50), unique=True, nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    photo = db.Column("photo", db.String(255))
    phone_number = db.Column("phone_number", db.String(255))
    email = db.Column("email", db.String(255))
    is_active = db.Column("is_active", db.Boolean, default=True)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    last_login = db.Column("last_login", db.DateTime)

    def __repr__(self) -> str:
        """
        Return a string representation of the user model.
        """

        return "<User >" % self.username

    def __str__(self) -> str:
        """
        Return a string representation of the user model.
        """

        return self.username

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the user model.
        """

        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'photo': self.photo,
            'phone_number': self.phone_number,
            'email': self.email,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'last_login': self.last_login
        }

    @classmethod
    def get_by_username(cls, username: str) -> "User":
        """
        Return a user model by username.
        """

        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_id(cls, id: int) -> "User":
        """
        Return a user model by id.
        """

        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_all(cls) -> "User":
        """
        Return all user models.
        """

        return cls.query.all()
    
    def save(self) -> None:
        """
        Save the user model.
        """

        db.session.add(self)
        db.session.commit()
    
    def delete(self) -> None:
        """
        Delete the user model.
        """

        db.session.delete(self)
        db.session.commit()
    
    def update(self, data: dict) -> None:
        """
        Update the user model.
        """

        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
