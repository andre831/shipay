from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

sql = SQLAlchemy()

dbc = sql.Column


class RoleModel(sql.Model):
    __tablename__ = "roles"

    id = dbc(sql.Integer, sql.Identity(always=True), primary_key=True)
    description = dbc(sql.String, nullable=False)

    def __init__(self, description):
        self.description = description


class ClaimModel(sql.Model):
    __tablename__ = "claims"

    id = dbc(sql.Integer, sql.Identity(always=True), primary_key=True)
    description = dbc(sql.String, nullable=False)
    active = dbc(sql.Boolean, nullable=False, default=True)

    def __init__(self, description, active=True):
        self.description = description
        self.active = active


class UserModel(sql.Model):
    __tablename__ = "users"

    id = dbc(sql.Integer, sql.Identity(always=True), primary_key=True)
    name = dbc(sql.String, nullable=False)
    email = dbc(sql.String, nullable=False)
    password = dbc(sql.String, nullable=False)
    role_id = dbc(sql.Integer, nullable=False)
    created_at = dbc(sql.DateTime, default=func.current_timestamp())
    updated_at = dbc(sql.DateTime, onupdate=func.current_timestamp())

    role = sql.relationship("RoleModel", backref="users")
    role_id = dbc(
        sql.Integer,
        sql.ForeignKey("roles.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )

    def __init__(self, name, email, password, role_id):
        self.name = name
        self.email = email
        self.password = password
        self.role_id = role_id


class UserClaimModel(sql.Model):
    __tablename__ = "user_claims"

    user_id = dbc(sql.Integer, nullable=False)
    claim_id = dbc(sql.Integer, nullable=False)

    __table_args__ = (
        sql.PrimaryKeyConstraint(user_id, claim_id),
        sql.ForeignKeyConstraint(
            [user_id],
            ["users.id"],
            name="user_claims_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sql.ForeignKeyConstraint(
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
