from flask import Flask
from flaskr.extensions import db, migrate, jwt, cors # Make sure db is imported!
from flask_cors import CORS

from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # This configuration is much more aggressive to ensure the headers are sent
    CORS(app, resources={r"/api/*": {
        "origins": ["http://localhost:5173"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }})

    # ... (Your configuration code like app.config['SQLALCHEMY_DATABASE_URI'] should be here)

    # THIS IS THE MISSING HANDSHAKE:
    db.init_app(app) 

    # Initialize your other tools
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    return app