import asyncio
from flask import Blueprint
import json

usersRoute = Blueprint("prefix", __name__, url_prefix="/users")


@usersRoute.route("/")
def get_all_users():
    data = {"name": "Andre"}

    return json.dumps(data)


@usersRoute.route("/register")
def post_new_user():
    return "ble"
