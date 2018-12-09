
import os


class Config:
    """Parent configuration class."""
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")

    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
