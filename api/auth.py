from flask import (
    jsonify,
    request
)

from models import User
from validators.auth import validate_user_register


def user_create():
    """
    Create a new user.

    :return: user model
    """

    if request.method == 'POST':
        data = request.get_json()
        validated_data = validate_user_register(data)
        if validated_data['message'] != "OK":
            return jsonify(validated_data), 400
        user = User(**validated_data['data'])
        password = validated_data['data']['password']
        user.set_password(password)
        user.save()
        return jsonify(user.to_dict()), 201
    return jsonify({
        'message': "Error: Method not allowed"
    }), 405
