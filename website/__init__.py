from flask import Flask
#flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='kkjjijkoklflewflpwfpwfwfwpfkpogreo'

#importing from the python packages the views.py and auth.py variables viewsname and authname
    from .views import viewsname
    from .auth import authname

#registering the blue prints
    app.register_blueprint(viewsname, url_prefix='/')
    app.register_blueprint(authname, url_prefix='/')

    return app