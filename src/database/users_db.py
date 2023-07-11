import asyncio
from models.main import sql, RoleModel, UserModel


class UsersDB:
    async def get_all_users(self):
        query = UserModel.query.all()

        return query

    async def get_only_user_by_role(self, role_id):
        user = UserModel.query.filter_by(role_id=role_id).first()

        role = RoleModel.query.filter_by(id=user.role_id).first()

        return role


users_db = UsersDB()
