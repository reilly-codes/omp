class Config:
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
    