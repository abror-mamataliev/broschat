from os.path import (
    abspath,
    dirname
)


DEBUG = True

HOST = "0.0.0.0"

PORT = 5001

PROJECT_FOLDER = abspath(dirname(dirname(__file__)))

SECRET_KEY = "secret"

SESSION_TYPE = "filesystem"

SQLALCHEMY_DATABASE_URI = "sqlite:///%s/database/db.sqlite" % PROJECT_FOLDER
SQLALCHEMY_TRACK_MODIFICATIONS = False
