from flask import Flask
from flask_misaka import markdown
from flask_misaka import Misaka
from config import DevServer
from posts.blueprint import posts



app = Flask(__name__)
app.register_blueprint(posts, url_prefix='/posts')

Misaka(app)

app.config.from_object(DevServer)