import markdown
from flask import Blueprint
import markdown.extensions.fenced_code


posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    test_file = posts.open_resource("posts/test.md","r")
    md_template_string = markdown.markdown(
        test_file.read(), extension=["fenced_code"]
    )
    return md_template_string