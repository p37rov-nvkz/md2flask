from flask import Blueprint
from flask import render_template



posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    file = open("posts/posts/test.md","r")
    mdf = file.read()
    
    return render_template("post.html", mdf = mdf)