from database.roles_db import RoleDB


class RoleCtrl:
    def __init__(self):
        pass

    async def get_all_roles():
        all_roles = await RoleDB.get_all_roles()

        roles = []

        for r in all_roles:
            r_data = {
                "id": r.id,
                "description": r.description,
            }

            roles.append(r_data)

        return roles

    async def create_role(data):
        new_role = await RoleDB.create_role(data)

        roles = []

        roles.append({"id": new_role.id, "description": new_role.description})

        return roles
