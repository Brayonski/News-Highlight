from flask import Flask
from config import config_options,DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    #create_app - function for taking configuration setting key as an argument

#Initialising application
    app = Flask(__name__)

#creating the app configurations
    app.config.from_object(config_options[config_name])

#Initialising flask extensions
    bootstrap.init_app(app)

#Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

#setting config
    from .request import configure_request
    configure_request(app)

    return app