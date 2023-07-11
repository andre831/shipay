import asyncio
import json
from flask import Blueprint, jsonify, request
from controller.users_control import users_ctrl

usersRoute = Blueprint("prefix", __name__, url_prefix="/users")


@usersRoute.route("/", methods=["GET"])
async def get_all_users():
    users = await users_ctrl.get_all_users()

    return jsonify(users)


@usersRoute.route("/role/<role_id>", methods=["GET"])
async def get_user_role(role_id):
    user = await users_ctrl.get_only_user_by_role(role_id)

    if user:
        return user
    else:
        return jsonify({"msg": "User not found"})
