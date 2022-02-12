class Config:
  """General configuration parent class"""
  QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

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