from src.routes.users import usersRoute
from flask import Flask

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(usersRoute)

if __name__ == "__main__":
    app.run(port=5000)
