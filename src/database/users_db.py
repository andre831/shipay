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

    async def create_user(self, data):
        new_user = UserModel(
            name=data["name"],
            email=data["email"],
            password=data.get("password"),
            role_id=data["role_id"],
        )

        # Salvar o novo usuário no banco de dados
        sql.session.add(new_user)
        sql.session.commit()

        return new_user


users_db = UsersDB()
