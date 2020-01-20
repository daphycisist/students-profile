con = sql.connect("students-profile.db")
con.execute("CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT)")
print("created table")
con.close()