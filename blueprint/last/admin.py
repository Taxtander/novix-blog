from flask import Blueprint, render_template, request, session, redirect, abort, url_for

import config
from models.product import Product
from utils import db

app = Blueprint("admin", __name__)


@app.before_request
def before_request():
    if session.get("admin_login", None) == None and request.endpoint != "main_blueprint.admin.admin_page":
        abort(403)


@app.route("/admin/login", methods=["GET", "POST"])
def admin_page():
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)

        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            session["admin_login"] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")

    return render_template("admin/login.html")


@app.route("/admin/dashboard", methods=["GET"])
def admin_dashboard_page():
    return render_template("/admin/dashboard.html")


@app.route("/admin/dashboard/product", methods=["GET", "POST"])
def admin_product_page():
    if request.method == "GET":
        product = Product.query.all()

        return render_template("/admin/product.html", product=product)
    else:
        name = request.form.get("name", None)
        description = request.form.get("description", None)
        price = request.form.get("price", None)
        active = request.form.get("active", None)
        file = request.files.get("cover", None)

        p = Product(name=name, description=description, price=price, active=1 if active else 0)

        db.session.add(p)
        db.session.commit()

        file.save(f'./static/cover/{p.id}.jpg')

        return "done"


@app.route("/admin/dashboard/product/edit-product/<id>", methods=["GET", "POST"])
def admin_edit_product_page(id):
    product = Product.query.filter(Product.id == id).first_or_404()

    if request.method == "GET":

        return render_template("/admin/edit-product.html", product=product)
    else:
        name = request.form.get("name", None)
        description = request.form.get("description", None)
        price = request.form.get("price", None)
        active = request.form.get("active", None)
        file = request.files.get("cover", None)

        product.name = name
        product.description = description
        product.price = price
        product.active = 1 if active else 0

        print(product.name, product.description, product.price, product.active)

        db.session.commit()

        if file!= None:
            file.save(f'static/cover/{product.id}.jpg')
        return redirect(url_for("main_blueprint.admin.admin_edit_product_page", id=id))
