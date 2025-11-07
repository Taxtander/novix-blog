from flask import Blueprint, render_template, request, session, redirect, abort, url_for

import config
from models.product import Product
from utils import db

app = Blueprint("admin", __name__)


@app.before_request
def before_request():
    pass



@app.route("/admin/login", methods=["GET", "POST"])
def admin_login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            session["admin_username"] = username
            return redirect(url_for("main_blueprint.admin.admin_dashboard_page"))

        else:
            return redirect(url_for("main_blueprint.admin.admin_login_page"))



    return render_template("admin/login.html")


@app.route("/admin/dashboard", methods=["GET"])
def admin_dashboard_page():
    return render_template("/admin/dashboard.html")


@app.route("/admin/dashboard/product", methods=["GET", "POST"])
def admin_product_page():


        return "done"


@app.route("/admin/dashboard/product/edit-product/<id>", methods=["GET", "POST"])
def admin_edit_product_page(id):
    pass
