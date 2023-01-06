from flask import Blueprint

hello_world = Blueprint('hello_world', __name__)


@hello_world.get("/")
def hello():
    """
    Returns the string "Hello there!"

    :return: Flask response
    """
    return 'Hello there!'