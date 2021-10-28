from flask import Flask
#from config import Config
from flask_login import LoginManager

flaskApp = Flask(__name__,template_folder='FrontEnd')
#app.config.from_object(Config)

login = LoginManager(flaskApp)
login.login_view = "login"

