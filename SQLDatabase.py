import sqlite3
import os


class MyDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("diagramdb.db")
        self.cursor = self.connection.cursor()
        print('Opened database!')

    def create_table(self, table_name):
        if self.check_table(table_name):
            print(table_name + " already exists")
        else:
            format_str = """
            CREATE TABLE {t_name} (
            file_number INTEGER PRIMARY KEY,
            file_name VARCHAR(30),
            file_content VARCHAR(999));"""
            sql_command = format_str.format(t_name=table_name)
            self.cursor.execute(sql_command)
            print('Table "' + table_name + '" created!')

    def add_data(self, table_name, file_number, file_name, file_content):
        if self.check_table(table_name):
            diagram_data = []
            diagram_data.append((file_number, file_name, file_content))
            for d in diagram_data:
                format_str = """INSERT INTO {t_name} (file_number, file_name, file_content)
                VALUES ("{number}", "{name}", "{content}");"""
                sql_command = format_str.format(t_name=table_name, number=d[0], name=d[1], content=d[2])
                self.cursor.execute(sql_command)
            self.connection.commit()
            print('Data added to "' + table_name + '"')
        else:
            print(table_name + " doesn't exist")

    def show_data(self, table_name):
        if self.check_table(table_name):
            format_str = """SELECT * FROM {t_name}"""
            sql_command = format_str.format(t_name=table_name)
            self.cursor.execute(sql_command)
            print("fetchall:")
            result = self.cursor.fetchall()
            for r in result:
                print(r)
            self.cursor.execute(sql_command)
            print("\nfetch one:")
            res = self.cursor.fetchone()
            print(res)
        else:
            print(table_name + " doesn't exist")

    def delete_table(self, table_name):
        if self.check_table(table_name):
            format_str = """DROP TABLE {t_name};"""
            sql_command = format_str.format(t_name=table_name)
            self.cursor.execute(sql_command)
            print('Table "' + table_name + '" deleted!')
        else:
            print(table_name + " doesn't exist")

    def check_table(self, table_name):
        self.cursor.execute(('''
        SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{t_name}'
        ''').format(t_name=table_name))
        if self.cursor.fetchone()[0] == 1:
            return True
        return False

    def close_database(self):
        self.connection.close()
        print('Closed database!')

    def delete_database(self):
        os.remove('diagramdb.db')
        print('Database deleted!')
