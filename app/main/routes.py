from flask import Blueprint

main = Blueprint('main',__name__)


# Routes
@main.route("/")
@main.route("/home")
def home():
    return "<h1> Welcome To Flask </h1>"