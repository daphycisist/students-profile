from flask import Flask, redirect, render_template, request
import csv
import sqlite3
import os



app = Flask(__name__)


@app.route("/")
def index():
    title = "Student Register"
    return render_template("index.html", title=title)


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


# students = []

@app.route("/register", methods=["POST", "GET"])
def registration():
    msg="msg"
    if request.method == "POST":
        try:
            firstname = request.form["firstname"]
            lastname = request.form["lastname"]
            email = request.form["email"]
            password = request.form["password"]
            # if not firstname or not lastname or not email or not password:
            #     return render_template("register.html")

            #working with databases
            with sqlite3.connect("students-profile.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (id, firstname, lastname) VALUES (?,?)",(firstname, lastname))
                con.commit()
                msg= "Record created successfully"
        except:
            con.rollback()
            msg = "Registration Failed"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

    
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
    

@app.route("/registrants")
def registrants():
    con=sqlite3.connect("students-profile.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()    
    
    #working with csv files
    # with open("registered.csv", "r") as file:
    #     reader = csv.reader(file)
    #     students = list(reader)
    return render_template("registered.html", rows=rows)
    # return render_template("registered.html", students=students)

# @app.route("/register", methods=["POST"])
# def registered():
#     firstname = request.form.get("firstname")
#     lastname = request.form.get("lastname")
#     email = request.form.get("email")
#     password = request.form.get("password")
#     if not firstname or not lastname or not email or not password:
#         return render_template("register.html")
#     return render_template("success.html")

