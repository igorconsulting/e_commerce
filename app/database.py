from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db

# Factory Pattern: This function sets up and initializes the database configuration.
def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Dependency Injection: The `db` instance is injected into the Flask app.

    with app.app_context():
        db.create_all()  # Ensures tables are created during initialization.
