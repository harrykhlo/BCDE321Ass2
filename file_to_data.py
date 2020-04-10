# this is a file for temporarily testing component
import ast
import os.path
from os import path
import inspect
import shelve

from pprint import pprint


# Harry's work
class FileToData(ast.NodeVisitor):
    """doctest
    >>> file_to_data = FileToData()
    >>> file_to_data.read_file("test.py")
    >>> file_to_data.show_ast_nodes()
    Module(body=[ClassDef(name='Car', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='door', ctx=Store())], value=Call(func=Name(id='Door', ctx=Load()), args=[Num(n=1)], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='wheel', ctx=Store())], value=Call(func=Name(id='Wheel', ctx=Load()), args=[Num(n=1)], keywords=[]))], decorator_list=[], returns=None), FunctionDef(name='is_sold', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Str(s='this car is sold')], keywords=[]))], decorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Door', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='number', ctx=Store())], value=Name(id='num', ctx=Load()))], decorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Wheel', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), arg(arg='num', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='number', ctx=Store())], value=Name(id='num', ctx=Load()))], decorator_list=[], returns=None)], decorator_list=[]), ClassDef(name='Taxi', bases=[Name(id='Car', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='color', ctx=Store())], value=Str(s='red'))], decorator_list=[], returns=None)], decorator_list=[])])

    >>> file_to_data = FileToData()
    >>> file_to_data.read_file("test.p")
    Your given python file does not exist in the current directory or your input arguments were wrong. The file name should be [py_file_name.py]. Please try again!
    """

    # Harry's work
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)
        # ast.NodeVisitor.visit(self, node)

    # Harry's work
    def read_file(self, file_name):
        try:
            if path.exists(file_name):
                with open(file_name, "r") as source:
                    self.tree = ast.parse(source.read())
            else:
                print("Your given python file does not exist in the current directory "
                      "or your input arguments were wrong. The file name "
                      "should be [py_file_name.py]. "
                      "Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def show_ast_nodes(self):
        print(ast.dump(self.tree))

    # Harry's work
    def show_all_classes(self):
        # print(ast.dump(self.tree))
        for my_class in self.tree.body:
            print(my_class.name)
        #     print("class:")
        #     print(tree.body[0].name) #Car class
        #     print("number of classes:")
        #     print(len(tree.body)) # show 4 classes

    # Harry's work
    def shelve_ast_nodes(self, file_name):
        db_file_name = file_name + ".db"
        try:
            if path.exists(file_name):
                with open(file_name, "r") as source:
                    self.tree = ast.parse(source.read())
                try:
                    shelve_tree = shelve.open(db_file_name)
                    shelve_tree[db_file_name] = self.tree
                except Exception as err:
                    print("Please try again! The exception is: ", err)
                finally:
                    shelve_tree.close()
            else:
                print("Your given python file does not exist in the current directory "
                      "or your input arguments were wrong. The file name "
                      "should be [py_file_name.py]. "
                      "Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def unshelve_ast_nodes(self, file_name):
        try:
            unshelve_object = shelve.open(file_name)
            self.tree = unshelve_object[file_name]
        except Exception as err:
            print("Please try again! The exception is: ", err)
        finally:
            unshelve_object.close()


    # Harry's work
if __name__ == "__main__":
    # ---below is for manual testing only
    # file_to_data = FileToData()
    # file_to_data.read_file("test.p")
    #file_to_data.show_ast_nodes()
    # file_to_data.show_all_classes()
    # ^^^below is for manual testing only

    # doctests
    import doctest
    doctest.testmod()


# with open("test.py", "r") as source:
#     # print(source.read())
#     print("----------------------------------------------")
#     tree = ast.parse(source.read())
#     print(ast.dump(tree))
#     print("----------------------------------------------")
#     print(tree.__dir__())
#     print("----------------------------------------------")
# # line below can get the
#     print("class:")
#     print(tree.body[0].name) #Car class
#     print("number of classes:")
#     print(len(tree.body)) # show 4 classes
#     print("----------------------------------------------")
#     print("function:")
#     print(tree.body[0].body[0].name)  # __init__ function
#     print("number of functions:")
#     print(len(tree.body[0].body)) # show 2 functions
#     print("----------------------------------------------")
#     print("Arguments in a function:")
#     print(tree.body[0].body[0].args.args[1].arg)  # num argument
#     print("Number of arguments including self:")
#     print(len(tree.body[0].body[0].args.args))  # show 2 arguments including self
#     print("----------------------------------------------")
#     print("Not sure what this is")
#     print(tree.body[0].body[0].args.vararg)  # None from vararg=None
#     print("----------------------------------------------")
#     print("Attributes in a class:")
#     print(tree.body[0].body[0].body[0].targets[0].attr)  # door attribute
#     print(tree.body[0].body[0].body[1].targets[0].attr)  # wheel attribute
#     print("number of attributes in a class:")
#     print(len(tree.body[0].body[0].body)) # show 2 attributes

# print(tree.body[0].ClassDef[0])
# print(inspect.getmembers(tree))
# print(tree[1])

# x = v()
# x.visit(tree)


#    for name in tree.names:
#        print(name)


# def main():
#     with open("test.py", "r") as source:
#         tree = ast.parse(source.read())
#     analyzer = Analyzer()
#     analyzer.visit(tree)
#     analyzer.report()
#
#
# class Analyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.stats = {"import": [], "from": []}
#
#     def visit_Import(self, node):
#         for alias in node.names:
#             self.stats["import"].append(alias.name)
#         self.generic_visit(node)
#
#     def visit_ImportFrom(self, node):
#         for alias in node.names:
#             self.stats["from"].append(alias.name)
#         self.generic_visit(node)
#
#     def report(self):
#         pprint(self.stats)
#
#
# if __name__ == "__main__":
#     main()
