import unittest
from DiagramCreator import MyCreator
from PickleMaker import MyPickle
from SQLDatabase import MyDatabase


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_validate_file(self):
        dc = MyCreator('ClassDiagram.png', 'TestClass.py')
        self.assertTrue(dc.validate_file_name())

    def test_check_table_false(self):
        sd = MyDatabase()
        self.assertFalse((sd.check_table('testtable')))

    def test_check_table_true(self):
        sd = MyDatabase()
        sd.create_table('testtable')
        self.assertTrue(sd.check_table('testtable'))
        sd.delete_table('testtable')


if __name__ == '__main__':
    unittest.main()
