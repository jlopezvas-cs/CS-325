from flask import Flask #type: ignore ##imported Flask
from flask import render_template # type: ignore ##imports render templates
from flask import request # type: ignore ##imports request
from flask import redirect #imports redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy.orm as so
import sqlalchemy as sa


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)  ##instance of the class
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db") #app.db defines the database filename
db = SQLAlchemy(app) #db object representing the database itself
migrate = Migrate(app, db)


class Log(db.Model):
     # define class variables
     id:so.Mapped[int] = so.mapped_column(primary_key = True)
     habit_name:so.Mapped[str] = so.mapped_column(index = True, default = "A Name")
     category:so.Mapped[str] = so.mapped_column(index = True, default = "Default Catergory")
     frequency:so.Mapped[str] = so.mapped_column(index = True, default = "Default Frequency")
     classification:so.Mapped[str] = so.mapped_column(index = True, default = "Default Classification")

    # The constructor
     def __init__(self):
         pass



a = Log()
a.habit_name = "Drinking Water"
a.category = "Health"

data = [ Log(), a ] #makes a list with an object in it

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/")  ##decorator route("/") that tells what URL should trigger the function
def home():
    return render_template('index.html')


@app.route("/log_habit", methods = ["GET", "POST"])
def log_habit():
    if request.method == 'GET':
        # do GET Stuff
        pass
    elif request.method == 'POST':
        # do POST Stuff
        pass

    return render_template("log_habit.html")

@app.route("/progress", methods=["GET", "POST"])
def progress():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        email = request.form["email"]
        print(f"Got POST request from {first_name} with email {email}")
   
    return render_template("progress.html", progress = data)

@app.route("/add_log")
def add_log():
    return render_template("form.html")

# @app.route("/submit-log", methods=['POST'])
# def submit_log():
#     first_name = request.form["first_name"]
#     email = request.form["email"]
#     print(first_name)
#     print(email)
#     print(f"Got POST request from {first_name} with email {email}")
#     return render_template('progress.html', progress=data) # you can also redirect if you want a different URL




##{% block body %}This is a block
##{% end block %}

##extend command {% extends 'whatever.html' %} This  command has to go at the beginning. 

