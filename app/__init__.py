from flask import Flask


def create_app(config_name):
    """
   app factory function
   :param config_name:
   :return: app
   """
    from .main import main

    app = Flask(__name__)
    app.register_blueprint(main)

    return app
