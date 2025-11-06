from flask import Blueprint, render_template
import models.user


app = Blueprint("user", __name__)


@app.route("/user/login")
def user_page():
    return render_template("user/login.html")
