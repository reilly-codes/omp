import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Myfamily@localhost/omp'

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'test':TestConfig,
    'production':ProdConfig
}
    