import sqlite3


class MyDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("diagramdb.db")
        self.cursor = self.connection.cursor()
        print('Opened database!')

    def create_table(self):
        sql_command = """
        CREATE TABLE diagram (
        file_number INTEGER PRIMARY KEY,
        file_name VARCHAR(30),
        file_content VARCHAR(999));"""
        self.cursor.execute(sql_command)

    def add_data(self, file_number, file_name, file_content):
        diagram_data = []
        diagram_data.append((file_number, file_name, file_content))
        for d in diagram_data:
            format_str = """INSERT INTO diagram (file_number, file_name, file_content)
            VALUES ("{number}", "{name}", "{content}");"""
            sql_command = format_str.format(number=d[0], name=d[1], content=d[2])
            self.cursor.execute(sql_command)
        self.connection.commit()

    def show_data(self):
        self.cursor.execute("SELECT * FROM diagram")
        print("fetchall:")
        result = self.cursor.fetchall()
        for r in result:
            print(r)
        self.cursor.execute("SELECT * FROM diagram")
        print("\nfetch one:")
        res = self.cursor.fetchone()
        print(res)

    def delete_table(self):
        self.cursor.execute("""DROP TABLE diagram;""")

    def close(self):
        self.connection.close()


sdb = MyDatabase()
sdb.create_table()
sdb.add_data(1, 'test', 'test content')
sdb.add_data(2, 'test2', 'test content2')
sdb.add_data(3, 'test3', 'test content3')
sdb.show_data()
sdb.delete_table()
sdb.close()



