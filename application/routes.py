from application import app
from flask import render_template, flash, redirect, url_for, get_flashed_messages


@app.route("/")
def index():       
    return render_template("index.html", title = "general")

@app.route("/props")
def props():
    return render_template("props.html",title = "props")

@app.route("/hoodie")
def hoodie():
    return render_template("hoodie.html",title = "hoodie")

@app.route("/hat")
def hat():
    return render_template("hat.html",title = "hat")

@app.route("/body")
def body():
    return render_template("body.html",title = "body")








