import random
import string

from database.users_db import UsersDB


class UsersCtrl:
    def __init__(self):
        pass

    def generate_random_password():
        letters_and_digits = string.ascii_letters + string.digits
        password = "".join(random.choice(letters_and_digits) for _ in range(12))
        return password

    @staticmethod
    async def get_all_users():
        users = await UsersDB.get_all_users()

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

    async def get_only_user_by_role(user_id, role_id):
        role_user = await UsersDB.get_only_user_by_role(user_id, role_id)

        user = []

        if role_user:
            u_data = {"id": role_user.id, "description": role_user.description}

            user.append(u_data)

            return user

        return []

    async def create_user(data):
        new_user = await UsersDB.create_user(data)

        print(new_user)

        user = []

        user.append(
            {
                "id": new_user.id,
                "name": new_user.name,
                "email": new_user.email,
                "password": new_user.password,
                "role_id": new_user.role_id,
                "created_at": new_user.created_at,
                "updated_at": new_user.updated_at,
            }
        )

        return user
