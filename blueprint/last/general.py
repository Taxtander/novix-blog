from flask import Blueprint, render_template, request

from models.post import Product

app = Blueprint("general", __name__)


@app.route("/")
def main_page():
    print(request.endpoint)
    products = Product.query.all()
    return render_template("general/main.html",products=products)

@app.route("/product/<int:id>/<name>")
def product_page(id,name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).filter(Product.active == 1).first_or_404()
    return render_template("general/post.html", product=product)
@app.route("/about")
def about_page():
    return render_template("general/about.html")


