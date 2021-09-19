import os
from flask import Flask, render_template, send_file
from flaskr.setup import login_manager, db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='nana7mi',
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
    login_manager.login_view = 'auth.login'

    # a simple page that says hello
    # @app.route('/', methods= ["GET"])
    # def index():
    #     return render_template('homepage.html')

    @app.route('/', methods=["GET"])
    def get_index():
        return send_file('./static/dist/index.html')

    @app.route('/js/<filename>', methods=["GET"])
    def get_js(filename):
        return send_file('./static/dist/js/{0}'.format(filename))

    @app.route('/css/<filename>', methods=["GET"])
    def get_css(filename):
        return send_file('./static/dist/css/{0}'.format(filename))

    @app.route('/img/<filename>', methods=["GET"])
    def get_img(filename):
        return send_file('./static/dist/img/{0}'.format(filename))

    @app.route('/favicon.ico', methods=["GET"])
    def get_ico():
        return send_file('./static/dist/favicon.ico')

    from . import auth
    app.register_blueprint(auth.bp)
    return app
