from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the SQLAlchemy object (database connector)
db = SQLAlchemy()
# Define the name of the SQLite database file.
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # A secret key is essential for securely signing session cookies and other security-related tasks.
    app.config['SECRET_KEY'] = 'DK123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import the application modules containing routes and logic
    from .views import views
    from .auth import auth

    # Register the Blueprints with the application
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import the database models to ensure SQLAlchemy knows what tables to create
    from .models import User, Note

    with app.app_context():
        db.create_all()

    # Initialize the LoginManager
    login_manager = LoginManager()
    # Flask-Login will redirect unauthenticated users here.
    login_manager.login_view = 'auth.login'
    # Initialize Flask-Login with the application
    login_manager.init_app(app)

    # This function is used to reload the user object from the session ID stored in the cookie.
    @login_manager.user_loader
    def load_user(id):
        """
                Retrieves a User object from the database using the user's ID.
                This is how Flask-Login keeps track of the current logged-in user.
                """
        return User.query.get(int(id)) #these three lines tell how flask login user

    # Return the fully configured Flask application instance
    return app


def create_database(app):
    """
        Checks if the database file exists and creates the tables if it does not.
        """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')