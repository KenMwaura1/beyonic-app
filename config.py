import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    class to holds main config for the app
    """
    BEYONIC_API_KEY = os.environ.get('BEYONIC_API_KEY')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig(Config):
    """
    production sub class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}
