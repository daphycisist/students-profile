from flask import Flask, redirect, render_template, request
import csv
import sqlite3
import os

app = Flask(__name__)
app.debug=True

@app.route("/")
def index():
    title = "Student Register"
    return render_template("index.html", title=title)

# students = []

@app.route("/register", methods=["POST", "GET"])
def registration():
    msg="msg"
    if request.method == "POST":
        try:
            #I can use this format to post to my database
            firstname = request.form.get("firstname")
            #or this
            lastname = request.form["lastname"]
            email = request.form["email"]
            password = request.form["password"]
            
            #working with databases
          
            
            with sqlite3.connect("students-profile.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (firstname, lastname) VALUES (?,?)",(firstname, lastname))
                con.commit()
                msg= "Record created successfully"
        except:
            con.rollback()
            msg = "Registration Failed"
        finally:
            return render_template("success.html", msg=msg)
            con.close()
    else:
        return render_template("register.html")

    
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

@app.route("/<rid>/delete", methods=["POST", "GET"])
def delete(rid):
    if request.method == "POST":
        con = sqlite3.connect("students-profile.db")
        cur=con.cursor()
        #for rid, a dangling comma is put after the rid to force a tuple. for better readability, we can employ the use of list literals [rid]
        cur.execute("DELETE FROM students WHERE id=(?)", (rid,))
        con.commit()
        return redirect("/registrants")
    else:
        return render_template("del_confirm.html", rid=rid)

if __name__ == "__main__":
    app.run()