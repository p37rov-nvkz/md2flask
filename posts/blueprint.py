from flask import Blueprint
from flask import render_template
from flask_misaka import markdown
from flask_misaka import Misaka


posts = Blueprint('posts', __name__, template_folder='templates')
Misaka(posts)

@posts.route('/')
def index():
    return "Blueprint Posts"