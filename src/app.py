import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from routes.users_routes import usersRoute
from routes.roles_routes import rolesRoute

from models.main import sql

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://shipay:shipay123@163.123.183.84:19653/shipayDB"

sql.init_app(app)
migrate = Migrate(app, sql, directory="models/migrations")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.register_blueprint(usersRoute, name="users")
app.register_blueprint(rolesRoute, name="roles")


@app.route("/")
def root():
    payload = {
        "msg": "Read the README.md",
        "link": "https://github.com/andre831/shipay/blob/main/README.md",
    }

    return json.dumps(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
