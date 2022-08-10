from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email
)

from models import User


class LoginForm(FlaskForm):
    """
    Login form

    Attributes:
        username: The username of the user.
        password: The password of the user.
    
    Methods:
        get_user: Get the user from the database.
    """

    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])

    def get_user(self) -> "User":
        """
        Get the user from the database.

        :return: The user.
        """
        
        return User.query.filter_by(username=self.username.data).first()


class RegisterForm(FlaskForm):
    """
    Register form

    Attributes:
        first_name: The first name of the user.
        last_name: The last name of the user.
        phone_number: The phone number of the user.
        email: The email of the user.
        username: The username of the user.
        password: The password of the user.
        password_confirm: The password confirmation of the user.
    """

    first_name = StringField("First name", validators=[DataRequired(), Length(min=5, max=50)])
    last_name = StringField("Last name")
    phone_number = StringField("Phone number", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    password_confirm = PasswordField("Confirm password", validators=[DataRequired(), Length(min=8)])
