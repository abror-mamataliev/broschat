from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from models import User


class LoginForm(FlaskForm):
    """
    Login form

    Attributes:
        username: The username of the user.
        password: The password of the user.
    """

    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])

    def get_user(self) -> "User":
        """
        Get the user from the database.

        :return: The user.
        """
        
        return User.query.filter_by(username=self.username.data).first()
