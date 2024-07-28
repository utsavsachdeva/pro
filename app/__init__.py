from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config   # Import configuration from config.py

# Create database instance (but don't initialize it yet)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# Function to create the Flask app
def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)  # Load configuration from Config class

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # Set the login page endpoint

    # Register blueprints
    from .blueprints import auth, admin, sponsor, influencer
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp, url_prefix='/admin')
    app.register_blueprint(sponsor.bp, url_prefix='/sponsor')
    app.register_blueprint(influencer.bp, url_prefix='/influencer')

    # Now it's safe to initialize Migrate
    migrate.init_app(app, db)

    return app
