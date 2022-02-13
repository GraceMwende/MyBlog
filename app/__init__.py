from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name): 
#initialize the application
  app = Flask(__name__)

  # creating up configuration
  app.config.from_object(config_options[config_name])

  # Initialize flask extensions
  bootstrap.init_app(app)
  db.init_app(app)  

  # setting config
  from .request import configure_request
  configure_request(app)

  # Registering blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  #will add views and forms
  # from app import views
  # from app import error
  return app