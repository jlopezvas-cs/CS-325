from flask import Flask #type: ignore ##imported Flask
from flask import render_template # type: ignore ##imports render templates
from flask import request # type: ignore ##imports request
from flask import redirect #imports redirect

class Log:
     # define class variables
     habit_name = "Default Name"
     category = "Default category"
     frequency = "Default frequency"
     classification = "Default type"

     def __init__(self):
         pass
     
a = Log()
a.habit_name = "Drinking Water"
a.category = "Health"

data = [ Log(), a ] #makes a list with an object in it



app = Flask(__name__)  ##instance of the class

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

@app.route("/progress")
def progress():
    return render_template("progress.html", progress = data)

@app.route("/add_log")
def add_log():
    return render_template("form.html")

@app.route("/submit-log", methods=['POST'])
def submit_log():
    first_name = request.form["first_name"]
    email = request.form["email"]
    print(first_name)
    print(email)
    print(f"Got POST request from {first_name} with email {email}")
    return "form submitted"




##{% block body %}This is a block
##{% end block %}

##extend command {% extends 'whatever.html' %} This  command has to go at the beginning. 

