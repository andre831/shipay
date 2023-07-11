import asyncio
import json
import random
import string
from flask import Blueprint, jsonify, request
from controller.users_control import users_ctrl

usersRoute = Blueprint("prefix", __name__, url_prefix="/users")


@usersRoute.route("/", methods=["GET"])
async def get_all_users():
    users = await users_ctrl.get_all_users()

    if users:
        return jsonify({"data": users}), 200
    else:
        return jsonify({"msg": "Users not found"}), 400


@usersRoute.route("/role/<role_id>", methods=["GET"])
async def get_user_role(role_id):
    user = await users_ctrl.get_only_user_by_role(role_id)

    if user:
        return jsonify({"data": user}), 200
    else:
        return jsonify({"msg": "User not found"}), 400


@usersRoute.route("/new", methods=["POST"])
async def new_user():
    data = request.json

    if "name" not in data or "email" not in data or "role_id" not in data:
        return jsonify({"msg": "Missing required fields"}), 400

    if "password" not in data:
        data["password"] = users_ctrl.generate_random_password()

    user = await users_ctrl.create_user(data)

    if user:
        return jsonify({"data": user}), 201
    else:
        return jsonify({"msg": "Failed to create user"}), 500
