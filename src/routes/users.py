import asyncio
from flask import Blueprint
import json

usersRoute = Blueprint("prefix", __name__, url_prefix="/users")


@usersRoute.route("/")
async def get_all_users():
    data = {"name": "Andre"}

    await asyncio.sleep(5)
    return json.dumps(data)


@usersRoute.route("/register")
def post_new_user():
    return "ble"
