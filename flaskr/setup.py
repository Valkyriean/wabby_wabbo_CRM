from flask_login import LoginManager
from flask_mongoengine import MongoEngine


db = MongoEngine()

login_manager = LoginManager()
login_manager.login_view = "auth.login"


