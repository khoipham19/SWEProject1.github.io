from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    return render_template("register.html")