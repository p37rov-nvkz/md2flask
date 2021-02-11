from flask import Flask
from config import DevServer
from posts.blueprint import posts



app = Flask(__name__)
app.register_blueprint(posts, url_prefix='/posts')

app.config.from_object(DevServer)