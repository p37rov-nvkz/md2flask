from flask import Flask
from config import DevServer



app = Flask(__name__)
app.config.from_object(DevServer)