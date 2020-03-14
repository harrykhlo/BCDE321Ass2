import ast

class datatodot:

    def __init__(self):
        self.classes_dict = {}

    def readdata(self, filename):
        with open(filename, "r") as source:
            self.sourcefromfile = source.read()


    def creatsourcetree(self):
        self.tree = ast.parse(self.sourcefromfile)


