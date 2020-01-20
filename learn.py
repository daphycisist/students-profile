from flask import Flask, redirect, render_template, request
import csv
import sqlite3 as sql
import os



app = Flask(__name__)


@app.route("/")
def index():
    title = "Student Register"
    # or
    return render_template("index.html", title=title)
    # return render_template("index.html")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


# students = []


@app.route("/registrants")
def registrants():
    
    
    #working with csv files
    # with open("registered.csv", "r") as file:
    #     reader = csv.reader(file)
    #     students = list(reader)
    return render_template("registered.html", students=students)
    # return render_template("registered.html", students=students)


@app.route("/register", methods=["POST"])
def registration():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password")
    if not firstname or not lastname or not email or not password:
        return render_template("register.html")
    
    
    #working with databases
    conn = sql.connect("students.db")
    conn.execute("CREATE TABLE  students (id INTEGER, firstname TEXT, lastname TEXT)")
    conn.close()

    
    
    
    # for working with .csv files
    
    # students.append(f"{lastname} {firstname}: {email}")
    # file = open("registered.csv", "a")
    # writer = csv.writer(file)
    # writer.writerow(([firstname, lastname]))
    # file.close()
    # return render_template("success.html")
    # or
    # return render_template("register.html")
    # students.append(f"{lastname} {firstname}: {email}")
    # return redirect("/registrants")

# @app.route("/register", methods=["POST"])
# def registered():
#     firstname = request.form.get("firstname")
#     lastname = request.form.get("lastname")
#     email = request.form.get("email")
#     password = request.form.get("password")
#     if not firstname or not lastname or not email or not password:
#         return render_template("register.html")
#     return render_template("success.html")
