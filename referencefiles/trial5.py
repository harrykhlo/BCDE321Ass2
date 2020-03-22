# from pylint import run_pyreverse
#
# run_pyreverse()

# from io import StringIO

# output = StringIO()
# print("a print out")
# contents = output.getvalue()
# output.close()
# print("{} second line".format(contents))


from file_to_data import FileToData
from io import StringIO
import sys

captured_output = StringIO()  # Create StringIO object
sys.stdout = captured_output  # and redirect stdout.
file_to_data = FileToData()
file_to_data.read_file("test.py")
file_to_data.show_ast_nodes()
sys.stdout = sys.__stdout__
Actual_output = captured_output.getvalue()
print("here " + Actual_output)
expected_output = "Module(body=[ClassDef(name='Car', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='door', ctx=Store())], value=Call(func=Name(id='Door', ctx=Load()), args=[Num(n=1)], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='wheel', ctx=Store())], value=Call(func=Name(id='Wheel', ctx=Load()), args=[Num(n=1)], keywords=[]))], decorator_list=[], returns=None), FunctionDef(name='is_sold', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Str(s='this car is sold')], keywords=[]))], decorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Door', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='number', ctx=Store())], value=Name(id='num', ctx=Load()))], decorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Wheel', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='number', ctx=Store())], value=Name(id='num', ctx=Load()))], decorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Taxi', bases=[Name(id='Car', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='color', ctx=Store())], value=Str(s='red'))], decorator_list=[], returns=None)], decorator_list=[])])\n"
print(Actual_output == expected_output)