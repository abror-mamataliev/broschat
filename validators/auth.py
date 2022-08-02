USER_LOGIN_SCHEMA = {
    'type': "object",
    'properties': {
        'username': {
            'type': "string",
            'minLength': 5,
            'maxLength': 50
        },
        'password': {
            'type': "string",
            'minLength': 8
        }
    },
    'required': [
        "username",
        "password"
    ]
}


USER_REGISTER_SCHEMA = {
    'type': "object",
    'properties': {
        'first_name': {
            'type': "string",
            'minLength': 5,
            'maxLength': 50
        },
        'last_name': {
            'type': "string",
            'minLength': 5,
            'maxLength': 50
        },
        'phone_number': {
            'type': "string"
        },
        'email': {
            'type': "string",
            'format': "email"
        },
        'username': {
            'type': "string",
            'minLength': 5,
            'maxLength': 50
        },
        'password': {
            'type': "string",
            'minLength': 8
        },
        'password_confirm': {
            'type': "string",
            'minLength': 8
        }
    },
    'required': [
        "first_name",
        "phone_number",
        "email",
        "username",
        "password",
        "password_confirm"
    ]
}
