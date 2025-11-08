from flask import Blueprint, render_template, request

from models.post import Post

app = Blueprint("general", __name__)


@app.route("/")
def main_page():
    posts = Post.query.all()
    return render_template("general/main.html", posts=posts)

@app.route("/post/<int:id>/<title>")
def post_page(id, title):
    post = Post.query.get_or_404(id)
    return render_template("general/post.html", post=post)

@app.route("/about")
def about_page():
    return render_template("general/about.html")


