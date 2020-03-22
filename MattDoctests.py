"""
>>> from DiagramCreator import MyCreator
>>> from PickleMaker import MyPickle
>>> from SQLDatabase import MyDatabase

>>> dc = MyCreator('ClassDiagram.png','TestClass.py')
Creating diagram...
>>> dc.validate_file_name()
True
>>> dc.create_diagram()
Diagram "ClassDiagram.png" created!
>>> dc.delete_diagram()
ClassDiagram.png deleted!

>>> pm = MyPickle('DoctestPickleFile.py','test')
Starting Pickle...
>>> pm.make_pickle()
DoctestPickleFile.py has been stored as test
>>> pm.unmake_pickle()
DoctestPickleFile.py
testfile = 1
<BLANKLINE>
>>> pm.delete_pickle()
test deleted!

>>> sd = MyDatabase()
Opened database!
>>> sd.create_table('testtable')
Table "testtable" created!
>>> sd.create_table('testtable')
testtable already exists
>>> sd.add_data('testtable', 1, 'testfile', 'test file content')
Data added to "testtable"
>>> sd.add_data('notatesttable', 1, 'testfile', 'test file content')
notatesttable doesn't exist
>>> sd.show_data('testtable')
fetchall:
(1, 'testfile', 'test file content')
<BLANKLINE>
fetch one:
(1, 'testfile', 'test file content')
>>> sd.show_data('notatesttable')
notatesttable doesn't exist
>>> sd.check_table('testtable')
True
>>> sd.check_table('notatesttable')
False
>>> sd.delete_table('testtable')
Table "testtable" deleted!
>>> sd.delete_table('notatesttable')
notatesttable doesn't exist
>>> sd.close_database()
Closed database!
>>> sd.delete_database()
Database deleted!
"""