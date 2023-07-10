from flask import Flask

from src.routes.users import usersRoute

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(usersRoute)

if __name__ == "__main__":
    app.run(port=5000)