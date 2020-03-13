from cmd import Cmd

class MyCli(Cmd):
    """Command line interpreter for generating UML class diagram"""

    def __init__(self, my_name = ">"):
        Cmd.__init__(self, my_name)
        self.my_name = my_name
        self.prompt = ">>" + my_name + ">> "

    def do_classdiagram(self, file_name):
        """Generate a class diagram in png format from [given file]"""
        self.file_name = file_name
        print(self.file_name)

    def help_classdiagram(self):
        print("\n".join(['Generate a class diagram in png format from [given file]', 
        'classdiagram [input source code file name] [output png file name])']))
        
        
    def do_quit(self, line):
        """Exit this command line interpreter"""
        print("Quitting......")
        return True
        
    def help_quit(self):
        print("\n".join(['Quit from this CLI', ':return: True']))


