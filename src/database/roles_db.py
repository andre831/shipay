from models.main import sql, RoleModel


class RoleDB:
    def __init__(self):
        pass

    async def get_all_roles():
        query = RoleModel.query.all()

        return query

    async def create_role(data):
        new_role = RoleModel(description=data["description"])

        sql.session.add(new_role)
        sql.session.commit()

        return new_role
