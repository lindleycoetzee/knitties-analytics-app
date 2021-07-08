from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///file.db"
# app.config["SECRET_KEY"] = "!!GETaHASH!!aawswdwewefewfwefferfvvvrevrevr"
#
# db = SQLAlchemy(app)

from application import routes
