from flask import Flask ##imported Flask
from flask import render_template ##imports render templates




app = Flask(__name__)  ##instance of the class

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/")  ##decorator route("/") that tells what URL should trigger the function
def home():
    return render_template('index.html')

@app.route("/log_habit")
def log_habit():
    return render_template("log_habit.html")

@app.route("/progress")
def progress():
    return render_template("progress.html")

@app.route("/test")
def test():
    return render_template("test.html")


##{% block body %}This is a block
##{% end block %}

##extend command {% extends 'whatever.html' %} This  command has to go at the beginning. 

