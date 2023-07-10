import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.routes.users import usersRoute
from src.database.models import database

app = Flask(__name__)
app.config.from_pyfile("database/config.py")

database.init_app(app)
migrate = Migrate(app, database, directory="database/migrations")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def root():
    payload = {
        "msg": "Read the README.md",
        "link": "https://github.com/andre831/shipay/blob/main/README.md",
    }

    return json.dumps(payload)


app.register_blueprint(usersRoute)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
