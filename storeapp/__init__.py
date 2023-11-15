#import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

#create a function that creates a web application
# a web server will run this web application
def create_app():
    app.debug = True
    app.secret_key = 'THEbestPASSword123456789'
    
    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fruitgarden.sqlite'

    #initialise db with flask app
    db.init_app(app)

    bootstrap = Bootstrap4(app)

   #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.main_bp)
    from . import admin
    app.register_blueprint(admin.admin_bp)
   
    return app

@app.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
  return render_template("404.html")

@app.errorhandler(500) 
# inbuilt function which takes error as parameter 
def not_found(e): 
  return render_template("500.html")