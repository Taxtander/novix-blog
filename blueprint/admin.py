from flask import Blueprint, render_template, request, session, redirect, url_for, flash,current_app

import config
from models.post import Post
from utils import db
import os
import uuid
import time

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



@app.route("/admin/dashboard/post/postpreview/<temp_id>")
def post_preview_page(temp_id):
    # Retrieve temporary content from session or cache
    temp_content = session.get(f"preview_content_{temp_id}", "")
    return render_template("/admin/post-preview.html", content=temp_content)


@app.route("/admin/dashboard/generate-preview", methods=["POST"])
def generate_preview():
    # Handle HTML file upload for preview
    html_file = request.files.get('content')
    if html_file and html_file.filename != '':
        html_content = html_file.read().decode('utf-8')
        temp_id = str(uuid.uuid4())
        session[f"preview_content_{temp_id}"] = html_content
        return {"success": True, "preview_url": url_for('main_blueprint.admin.post_preview_page', temp_id=temp_id)}
    
    return {"success": False, "error": "No file provided"}


@app.route("/admin/dashboard/create-post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        keywords = request.form.get("keywords")
        html_content = ""

        html_file = request.files.get("content")
        if html_file and html_file.filename != "":
            html_content = html_file.read().decode("utf-8")

        html_folder = os.path.join(current_app.root_path, "static", "HTML-POSTS")
        if not os.path.exists(html_folder):
            os.makedirs(html_folder)

        filename = f"{title}-{str(uuid.uuid4())[:8]}.html".replace(" ", "-")
        relative_path = os.path.join("HTML-POSTS", filename)
        full_path = os.path.join(html_folder, filename)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        if title and keywords and html_content:
            new_post = Post(title=title, content_name=relative_path, keywords=keywords)
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
