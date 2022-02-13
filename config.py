import os

class Config:
  """General configuration parent class"""
  QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SECRET_KEY=os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql + psycog2://moringa:Access@localhost/myblog'

class ProdConfig(Config):
  """Production configuration class
  Args:
      Config:Tha parent configuratuon class with General configuraton settings
  """
  pass

class DevConfig(Config):
  """Development configuration class
  Args:
      Config:The parent configuration class with General configuration settings
  """
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' : ProdConfig
}