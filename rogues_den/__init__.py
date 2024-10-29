import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from .models import User, Character
# from .database import db
if os.path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')

# db.init_app(app)

db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'views.dashboard'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# from rogues_den import routes
