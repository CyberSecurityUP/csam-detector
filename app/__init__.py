from flask import Flask
from app.routes import main_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secure-key"  # altere para produção
    app.register_blueprint(main_routes)
    return app
