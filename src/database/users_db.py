import asyncio
from models.main import UserModel


class UsersDB:
    async def get_all_users(self):
        query = UserModel.query.all()

        return query

    async def get_only_user_by_role(self, role_id):
        query = UserModel.query.filter_by(role_id=role_id).first()

        if query:
            return query
        else:
            return None


users_db = UsersDB()
