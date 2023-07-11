import asyncio
from models.main import sql, RoleModel, UserModel


class UsersDB:
    def __init__(self):
        pass

    async def get_all_users():
        query = UserModel.query.all()

        return query

    async def get_only_user_by_role(user_id, role_id):
        user = UserModel.query.filter_by(id=user_id, role_id=role_id).first()

        if user:
            role = RoleModel.query.filter_by(id=user.role_id).first()

            if role:
                return role

        return None

    async def create_user(data):
        new_user = UserModel(
            name=data["name"],
            email=data["email"],
            password=data.get("password"),
            role_id=data["role_id"],
        )

        sql.session.add(new_user)
        sql.session.commit()

        return new_user


users_db = UsersDB()
