from cmd import Cmd
import subprocess

class MyCli(Cmd):
    """Command line interpreter for generating UML class diagram"""

    def __init__(self, my_name = ">"):
        Cmd.__init__(self, my_name)
        self.my_name = my_name
        self.prompt = ">>" + my_name + ">> "

    def do_pyrclassdiagram(self, file_names):
        """Generate a class diagram in png format from given [png_file_name_suffix py_file_name.py]"""
        self.file_names = file_names
        pyreverse_command = 'pyreverse -ASmn -o png -p ' + file_names
        #subprocess.call(shlex.split(pyreverse_command))
        subprocess.call(pyreverse_command)
        print(file_names + ' are done')

    def help_pyrclassdiagram(self):
        print("\n".join(['Generate a class diagram in png format from given file',
        'classdiagram [output png file name suffix] [input source code file name.py] )']))

    def do_quit(self, line):
        """Exit this command line interpreter"""
        print("Quitting......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from this CLI', ':return: True']))

if __name__ == '__main__':
    my_cli = MyCli()
    my_cli.cmdloop()
