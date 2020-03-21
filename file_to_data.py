# this is a file for temporarily testing component
import ast
import os.path
from os import path
import inspect

from pprint import pprint


# Harry's work
class FileToData(ast.NodeVisitor):

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

    def show_ast_nodes(self):
        print(ast.dump(self.tree))

    def show_all_classes(self):
        # print(ast.dump(self.tree))
        for my_class in self.tree.body:
            print(my_class.name)
        #     print("class:")
        #     print(tree.body[0].name) #Car class
        #     print("number of classes:")
        #     print(len(tree.body)) # show 4 classes


# below is for testing only
if __name__ == "__main__":
    file_to_data = FileToData()
    file_to_data.readfile("test.py")
    file_to_data.show_ast_nodes()
    file_to_data.show_all_classes()

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
