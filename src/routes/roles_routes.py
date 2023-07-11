from flask import Blueprint, jsonify, request
from controller.roles_control import RoleCtrl

rolesRoute = Blueprint("role", __name__, url_prefix="/roles")


@rolesRoute.route("/", methods=["GET"])
async def get_all_roles():
    roles = await RoleCtrl.get_all_roles()

    if roles:
        return jsonify({"data": roles}), 200
    else:
        return jsonify({"msg": "Roles not found"}), 400


@rolesRoute.route("/new", methods=["POST"])
async def new_role():
    data = request.json

    if "description" not in data:
        return jsonify({"msg": "Missing required field"}), 400

    role = await RoleCtrl.create_role(data)

    if role:
        return jsonify({"data": role}), 201
    else:
        return jsonify({"msg": "Failed to create role"}), 500
