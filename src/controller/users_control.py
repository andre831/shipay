import random
import string

from database.users_db import users_db


class UsersCtrl:
    async def get_all_users():
        users = await users_db.get_all_users()

        all_users = []

        if len(users) < 1:
            return []

        for u in users:
            u_data = {
                "id": u.id,
                "name": u.name,
                "email": u.email,
                "password": u.password,
                "role_id": u.role_id,
                "created_at": u.created_at,
                "updated_at": u.updated_at,
            }

            all_users.append(u_data)

        return all_users

    async def get_only_user_by_role(role_id):
        role_user = await users_db.get_only_user_by_role(role_id)

        user = []

        if role_user:
            u_data = {"id": role_user.id, "description": role_user.description}

            user.append(u_data)

            return user

        return []


users_ctrl = UsersCtrl
