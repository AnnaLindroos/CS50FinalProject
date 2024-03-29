import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

app.url_map.strict_slashes=False

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///discgolf.db")

@app.route("/")
def index():

    discgolfFirst = db.execute("SELECT * FROM discgolf ORDER BY RANDOM() LIMIT 1")
    double = discgolfFirst[0].get("id")

    discgolfSecond = db.execute("SELECT * FROM discgolf WHERE id != ? ORDER BY RANDOM() LIMIT 1", double)

    return render_template("index.html", first=discgolfFirst[0], second=discgolfSecond[0])