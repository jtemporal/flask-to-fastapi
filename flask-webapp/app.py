from flask import Flask

from auth.views import auth_bp
from config import config
from webapp.views import webapp_bp
from utils import to_pretty_json


app = Flask(__name__)
app.secret_key = config["WEBAPP"]["SECRET_KEY"]
app.jinja_env.filters['to_pretty_json'] = to_pretty_json

app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(webapp_bp, url_prefix='/')
