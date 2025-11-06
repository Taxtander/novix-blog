from flask import Blueprint, render_template, request, session, redirect, abort, url_for

import config
from models.product import Product
from utils import db

app = Blueprint("admin", __name__)


@app.before_request
def before_request():
    pass



@app.route("/admin/login", methods=["GET", "POST"])
def admin_page():


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
