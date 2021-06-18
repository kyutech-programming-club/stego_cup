from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

from app.controllers.home import bp
app.register_blueprint(bp)

