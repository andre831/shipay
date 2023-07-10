from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

dbc = database.Column


class RoleModel(database.Model):
    __tablename__ = "roles"

    id = dbc(database.Integer, database.Identity(always=True), primary_key=True)
    description = dbc(database.String, nullable=False)

    def __init__(self, description):
        self.description = description


class ClaimModel(database.Model):
    __tablename__ = "claims"

    id = dbc(database.Integer, database.Identity(always=True), primary_key=True)
    description = dbc(database.String, nullable=False)
    active = dbc(database.Boolean, nullable=False, default=True)

    def __init__(self, description, active=True):
        self.description = description
        self.active = active


class UserModel(database.Model):
    __tablename__ = "users"

    id = dbc(database.Integer, database.Identity(always=True), primary_key=True)
    name = dbc(database.String, nullable=False)
    email = dbc(database.String, nullable=False)
    password = dbc(database.String, nullable=False)
    role_id = dbc(database.Integer, nullable=False)
    created_at = dbc(database.DateTime, default=func.current_timestamp())
    updated_at = dbc(database.DateTime, onupdate=func.current_timestamp())

    def __init__(self, name, email, password, role_id):
        self.name = name
        self.email = email
        self.password = password
        self.role_id = role_id


# ForeignKey constraints
database.ForeignKeyConstraint(
    ["role_id"], ["roles.id"], name="users_fk", onupdate="CASCADE", ondelete="CASCADE"
)


class UserClaimModel(database.Model):
    __tablename__ = "user_claims"

    user_id = dbc(database.Integer, nullable=False)
    claim_id = dbc(database.Integer, nullable=False)

    __table_args__ = (
        database.PrimaryKeyConstraint(user_id, claim_id),
        database.ForeignKeyConstraint(
            [user_id],
            ["users.id"],
            name="user_claims_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        database.ForeignKeyConstraint(
            [claim_id],
            ["claims.id"],
            name="user_claims_fk_1",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
    )

    def __init__(self, user_id, claim_id):
        self.user_id = user_id
        self.claim_id = claim_id
