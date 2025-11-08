from flask import Blueprint, render_template, request, session, redirect, url_for, flash
import config
from models.post import Post
from utils import db

app = Blueprint("admin", __name__)


@app.before_request
def before_request():
    if request.endpoint and request.endpoint.startswith("main_blueprint.admin."):
        if session.get("admin_login") is None and request.endpoint != "main_blueprint.admin.admin_login_page":
            return redirect(url_for("main_blueprint.admin.admin_login_page"))


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            session["admin_login"] = username
            return redirect(url_for("main_blueprint.admin.admin_dashboard_page"))
        else:
            flash('Invalid credentials', 'error')
            return redirect(url_for("main_blueprint.admin.admin_login_page"))

    return render_template("admin/login.html")


@app.route("/admin/dashboard", methods=["GET"])
def admin_dashboard_page():
    posts = Post.query.all()
    return render_template("/admin/dashboard.html", posts=posts)


@app.route("/admin/dashboard/posts", methods=["GET"])
def admin_posts_page():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("/admin/posts.html", posts=posts)


@app.route("/admin/dashboard/post", methods=["GET", "POST"])
def admin_create_post_page():
    # This route now handles the blog post creation form
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        
        if title and content:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('main_blueprint.admin.admin_dashboard_page'))
        else:
            flash('Please fill in all fields', 'error')
    
    return render_template("/admin/post.html")


@app.route("/admin/dashboard/create-post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        
        if title and content:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('main_blueprint.admin.admin_dashboard_page'))
        else:
            flash('Please fill in all fields', 'error')
    
    return render_template("/admin/create-post.html")


@app.route("/admin/dashboard/edit-post/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    post = Post.query.get_or_404(id)
    
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        
        if title and content:
            post.title = title
            post.content = content
            db.session.commit()
            flash('Post updated successfully!', 'success')
            return redirect(url_for('main_blueprint.admin.admin_dashboard_page'))
        else:
            flash('Please fill in all fields', 'error')
    
    return render_template("/admin/edit-post.html", post=post)


@app.route("/admin/dashboard/delete-post/<int:id>", methods=["POST"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main_blueprint.admin.admin_dashboard_page'))


@app.route("/admin/dashboard/product/edit-product/<id>", methods=["GET", "POST"])
def admin_edit_product_page(id):
    # TODO: Implement product editing functionality
    pass
