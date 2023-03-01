from flask import Blueprint, render_template

authname = Blueprint('authname', __name__)

@authname.route('/login')
def login():
    return render_template("login.html")

@authname.route('/logout')
def logout():
    return "<p>Logout</p>"

@authname.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
