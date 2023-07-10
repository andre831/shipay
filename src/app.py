import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from routes.users import usersRoute
from models.main import sql

app = Flask(__name__)
app.config.from_pyfile("models/config.py")

sql.init_app(app)
migrate = Migrate(app, sql, directory="models/migrations")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.register_blueprint(usersRoute)


@app.route("/")
def root():
    payload = {
        "msg": "Read the README.md",
        "link": "https://github.com/andre831/shipay/blob/main/README.md",
    }

    return json.dumps(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
