from flask import Flask
from config import Config
from evmstore.routes.index import bp as index_bp
from evmstore.routes.add import bp as add_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(index_bp)
    app.register_blueprint(add_bp)

    return app
