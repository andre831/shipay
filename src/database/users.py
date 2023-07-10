from sqlalchemy import func
from database.config import database

dbc = database.Column


class UserModel(database.Model):
    __tablename__ = "users"

    id = dbc(database.Integer, database.Identity(always=True), primary_key=True)
    name = dbc(database.String(), nullable=False)
    email = dbc(database.String(), nullable=False)
    password = dbc(database.String(), nullable=False)
    role_id = dbc(database.Integer(), database.ForeignKey("parent.id"), nullable=False)
    created_at = dbc(database.DateTime, default=func.current_timestamp())
    updated_at = dbc(
        database.DateTime,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    def __init__(self, name, email, password, role_id):
        self.name = name
        self.email = email
        self.password = password
        self.role_id = role_id
