import os
from flask import Flask, render_template
from flaskr.setup import login_manager, db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['MONGODB_SETTINGS'] = {
        "db": "crm",
        'host': 'localhost',
        'port': 27017

    }

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('homepage.html')


    from . import auth
    app.register_blueprint(auth.bp)
    
    return app