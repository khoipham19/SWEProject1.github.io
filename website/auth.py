from flask import Blueprint, render_template, request, flash, redirect, url_for
from .login import login, signup, check_user_validity, check_user_exists
from .app import fridge, index

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        is_valid = check_user_validity(email, password)
        print(is_valid)
        if is_valid == False:
             print(password)
             flash('Incorrect email or password', 'error')
        else:
            login(email, password)
            return redirect(url_for('fridge.index'))

    return render_template("login.html", bool=True)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        is_valid = check_user_exists(email, password)
        if is_valid == False:
            flash('User already exists', 'error')
        else:
            signup(email, password)
            return redirect(url_for('auth.account_made'))
            

    return render_template("register.html")

@auth.route('/account_made')
def account_made():
    return render_template("account_made.html")