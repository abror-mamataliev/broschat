from jsonschema import validate

from models import User
from schemas import (
    USER_LOGIN_SCHEMA,
    USER_REGISTER_SCHEMA
)


def validate_user_register(data: dict) -> dict:
    """
    Validate user registration data.

    :param data: user registration data
    :return: validated data
    """

    try:
        validate(data, USER_REGISTER_SCHEMA)
    except Exception as e:
        return {
            'data': data,
            'message': f"Error: {str(e)}"
        }
    user = User.get_by_username(data['username'])
    if user is not None:
        return {
            'data': data,
            'message': "Error: User already exists"
        }
    password = data['password']
    password_confirm = data['password_confirm']
    if password != password_confirm:
        return {
            'data': data,
            'message': "Error: Passwords do not match"
        }
    response = {
        'data': {},
        'message': "OK"
    }
    for key, value in data.items():
        if key != 'password_confirm':
            response['data'][key] = value
    return response
