from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def db_config(app):
    db.init_app(app)
