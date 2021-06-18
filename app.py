from flask import Flask

from admin import init_admin
from config import load_config
from routes import init_routes
from storage import create_database, init_database


def create_app():
    app = Flask(__name__)
    app = load_config(app)
    app = init_database(app)
    app = init_admin(app)
    app = create_database(app)
    app = init_routes(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
