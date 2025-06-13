from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/to_do_list'
    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, register_blueprint='/')
    app.register_blueprint(views, register_blueprint='/')

    from .models import User_Name, Item

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User_Name.query.get(int(id))
    
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Database created')
