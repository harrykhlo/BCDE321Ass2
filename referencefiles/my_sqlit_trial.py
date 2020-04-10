import sqlite3



try:
    conn = sqlite3.connect('my_sqlite.db')
except Exception as err:
    print("Please try again! The exception is: ", err)
else:
    print("Database at my_sqlite.db is connected")


c = conn.cursor()

# c.execute("""CREATE TABLE mytable (
#                 classname text,
#                 numoffunction integer
#                 )""")
# c.execute("INSERT INTO mytable VALUES ('{}', {})".format(my_file.class_name, my_file.num_of_function))
# c.execute("INSERT INTO mytable VALUES ('Class1', 3)")
# c.execute("INSERT INTO mytable VALUES ('Class2', 4)")
c.execute("SELECT * FROM mytable")
print(c.fetchall())

conn.commit()

conn.close()

