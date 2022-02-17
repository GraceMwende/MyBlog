import os

class Config:
  """General configuration parent class"""
  QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SECRET_KEY=os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/myblog'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # Email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME= os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  # simple mde  configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

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