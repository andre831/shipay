from flask import Blueprint, jsonify, request
from controller.users_control import UsersCtrl

usersRoute = Blueprint("users", __name__, url_prefix="/users")


@usersRoute.route("/", methods=["GET"])
async def get_all_users():
    users = await UsersCtrl.get_all_users()

    if users:
        return jsonify({"data": users}), 200
    else:
        return jsonify({"msg": "Users not found"}), 400


@usersRoute.route("<user_id>/role/<role_id>", methods=["GET"])
async def get_user_role(user_id, role_id):
    user = await UsersCtrl.get_only_user_by_role(user_id, role_id)

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
        data["password"] = UsersCtrl.generate_random_password()

    user = await UsersCtrl.create_user(data)

    if user:
        return jsonify({"data": user}), 201
    else:
        return jsonify({"msg": "Failed to create user"}), 500
