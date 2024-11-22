from flask import Flask
from app.routes import routes
from app.database import init_db

# Builder Pattern: The Flask app is configured step-by-step before being run.
app = Flask(__name__)
init_db(app)  # Dependency Injection: Database configuration is injected here.

# Register routes using Blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
