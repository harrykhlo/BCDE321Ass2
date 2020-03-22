import unittest
from file_to_data import FileToData
from io import StringIO
import sys


class MyTestCase(unittest.TestCase):
    def test_show_ast_nodes(self):
        captured_output = StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        file_to_data = FileToData()
        file_to_data.read_file("test.py")
        file_to_data.show_ast_nodes()
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = "Module(body=[ClassDef(name='Car', bases=[], keywords=[], body=[FunctionDef(" \
                          "name='__init__', args=arguments(args=[arg(arg='self', annotation=None), " \
                          "arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], " \
                          "kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', " \
                          "ctx=Load()), attr='door', ctx=Store())], value=Call(func=Name(id='Door', ctx=Load()), " \
                          "args=[Num(n=1)], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', " \
                          "ctx=Load()), attr='wheel', ctx=Store())], value=Call(func=Name(id='Wheel', ctx=Load()), " \
                          "args=[Num(n=1)], keywords=[]))], decorator_list=[], returns=None), FunctionDef(" \
                          "name='is_sold', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, " \
                          "kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name" \
                          "(id='print', ctx=Load()), args=[Str(s='this car is sold')], keywords=[]))], d" \
                          "ecorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Door', " \
                          "bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=" \
                          "[arg(arg='self', annotation=None), arg(arg='num', annotation=None)], vararg=None, " \
                          "kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=" \
                          "[Attribute(value=Name(id='self', ctx=Load()), attr='number', ctx=Store())], " \
                          "value=Name(id='num', ctx=Load()))], decorator_list=[], returns=None)], " \
                          "decorator_list=[]), ClassDef(name='Wheel', bases=[], keywords=[], body=[FunctionDef" \
                          "(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), " \
                          "arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], " \
                          "kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', " \
                          "ctx=Load()), attr='number', ctx=Store())], value=Name(id='num', ctx=Load()))], " \
                          "decorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Taxi', " \
                          "bases=[Name(id='Car', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', " \
                          "args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], " \
                          "kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='super', " \
                          "ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', " \
                          "ctx=Load()), attr='color', ctx=Store())], value=Str(s='red'))], decorator_list=[], " \
                          "returns=None)], decorator_list=[])])\n"

        self.assertEqual(actual_output, expected_output)

    def test_read_file_wrong_file_name(self):
        captured_output = StringIO()  # Create StringIO object
        sys.stdout = captured_output  # and redirect stdout.
        file_to_data = FileToData()
        file_to_data.read_file("test.p")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = "Your given python file does not exist in the current directory or your input " \
                          "arguments were wrong. The file name should be [py_file_name.py]. Please try again!\n"

        actual_output = 0

        expected_output = 0
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
