from flask import Blueprint


posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    return "Blueprint Posts"