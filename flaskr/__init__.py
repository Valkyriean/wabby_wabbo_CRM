import os
from flask import Flask, send_file
from flask_mongoengine import MongoEngine
from flask_cors import CORS
# from secret import *
# from flask_wtf.csrf import CSRFProtect


# csrf = CSRFProtect()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', None)
    )
    app.config['MONGODB_HOST'] = 'mongodb+srv://' + os.environ.get('DB_USERNAME', None) + ':' + os.environ.get(
        'DB_PASSWORD', None) + '@cluster0.gixca.mongodb.net/crm?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE'

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

    db = MongoEngine()
    db.init_app(app)
    # csrf.init_app(app)

    # Serve the static file to client's browser
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

    @app.route('/media/<filename>', methods=["GET"])
    def get_media(filename):
        return send_file('./static/dist/media/{0}'.format(filename))

    @app.route('/favicon.ico', methods=["GET"])
    def get_ico():
        return send_file('./static/dist/favicon.ico')

    @app.route('/app/<foo>', methods=["GET"])
    def serve(foo):
        return send_file('./static/dist/index.html')

    @app.route('/app/<foo>/<bar>', methods=["GET"])
    def serve1(foo, bar):
        return send_file('./static/dist/index.html')

    from . import auth
    app.register_blueprint(auth.bp)
    from . import dashboard
    app.register_blueprint(dashboard.bp)
    from . import form
    app.register_blueprint(form.bp)
    return app
