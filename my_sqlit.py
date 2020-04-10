import sqlite3

class MySqlit:

    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.conn = sqlite3.connect(self.file_name) #e.g. file_name = 'my_sqlite.db'
        except Exception as err:
            print("Please try again! The exception is: ", err)
        else:
            print("Database at my_sqlite.db is connected")

    def close_connection(self):
        self.conn.close()
        print('mytable is closed')

    def commit_connection(self):
        self.conn.commit()
        print('mytable is committed')

    def create_my_table(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("""CREATE TABLE IF NOT EXISTS mytable (
                             classname text,
                             numoffunction integer
                             )""")
        #self.conn.commit()
        print('mytable is created if not exists')

    def drop_my_table(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("""DROP TABLE IF EXISTS mytable""")
        #self.conn.commit()
        print('mytable is dropped if exists')

    def my_insert(self, class_name, num_of_functions):
        my_cursor = self.conn.cursor()
        my_cursor.execute("INSERT INTO mytable VALUES ('{}', {})".format(class_name, num_of_functions))
        print("Inserted the class name ({}) and number of functions ({}) into mytable of {} database."
              .format(class_name, num_of_functions, self.file_name))

    def fetch_all_my_table(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("SELECT * FROM mytable")
        print("All classes and its number of functions are listed below:")
        print(my_cursor.fetchall())

# try:
#     conn = sqlite3.connect('my_sqlite.db')
# except Exception as err:
#     print("Please try again! The exception is: ", err)
# else:
#     print("Database at my_sqlite.db is connected")
#
#
# c = conn.cursor()

# c.execute("""CREATE TABLE mytable (
#                 classname text,
#                 numoffunction integer
#                 )""")
# c.execute("INSERT INTO mytable VALUES ('{}', {})".format(my_file.class_name, my_file.num_of_function))
# c.execute("INSERT INTO mytable VALUES ('Class1', 3)")
# c.execute("INSERT INTO mytable VALUES ('Class2', 4)")
# c.execute("SELECT * FROM mytable")
# print(c.fetchall())

# conn.commit()
#
# conn.close()

# below is for manual testing only
if __name__ == '__main__':
    my_sqlit = MySqlit('my_sqlite.db')
    # my_sqlit.drop_my_table()
    # my_sqlit.create_my_table()
    # my_sqlit.my_insert('HarryClass',3)
    # my_sqlit.my_insert('MaryClass', 3)
    # my_sqlit.my_insert('PeterClass', 3)
    my_sqlit.fetch_all_my_table()
    my_sqlit.commit_connection()
    my_sqlit.close_connection()