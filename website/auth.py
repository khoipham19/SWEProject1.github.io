from flask import Blueprint, render_template, request, flash
from .login import login, signup
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        login(email, password)
        return render_template("account_made.html")

    return render_template("login.html", boolean =True)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if len(email) < 4:
            flash('Email invalid', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters', category = 'error')
        else:
            signup(email, password)
            return render_template("account_made.html")
            

    return render_template("register.html")

@auth.route('/account_made')
def account_made():
    return render_template("account_made.html")