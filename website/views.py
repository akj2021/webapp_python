from flask import Blueprint, render_template

#defintion of application blueprints - with roots 
viewsname = Blueprint('viewsname', __name__)

@viewsname.route('/') #defines a view
def home():
    return render_template("home.html")