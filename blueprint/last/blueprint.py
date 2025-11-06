from flask import Blueprint
from .general import app as general_bp
from .admin import app as admin_bp
from .user import app as user_bp

app = Blueprint("main_blueprint", __name__)

app.register_blueprint(general_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
