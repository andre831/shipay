import asyncio
import json
from flask import Blueprint, jsonify
from src.controller.users_control import users_ctrl

usersRoute = Blueprint("prefix", __name__, url_prefix="/users")


@usersRoute.route("/", methods=["GET"])
async def get_all_users():
    users = await users_ctrl.get_all_users()

    return jsonify(users)


@usersRoute.route("/role/<role_id>", methods=["GET"])
async def get_user_role(role_id):
    user = await users_ctrl.get_only_user_by_role(1, role_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"msg": "User not found"})


@usersRoute.route("/register", methods=["POST"])
def post_new_user():
    return "ble"
