from flask import Flask
from blueprint.blueprint import app as blueprint_app
from flask_sqlalchemy import SQLAlchemy
import config
import utils
from models.user import User
from flask_login import LoginManager

app = Flask(__name__)
app.register_blueprint(blueprint_app)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
utils.db.init_app(app)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
