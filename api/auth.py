from flask import (
    jsonify,
    request
)

from models import User


def user_create():
    """
    Create a new user.
    """

    if request.method == 'POST':
        data = request.get_json()
        if data.get('password') == data.get('password_confirm'):
            user = User(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                phone_number=data.get('phone_number'),
                email=data.get('email'),
                username=data.get('username')
            )
            user.set_password(data.get('password'))
            user.save()
            return jsonify(user.to_dict()), 201
        return jsonify({
            'message': "Passwords do not match"
        }), 400
    return jsonify({
        'message': "Method not allowed"
    }), 405
