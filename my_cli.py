from cmd import Cmd
import subprocess
from file_to_data import FileToData
import webbrowser


class MyCli(Cmd):
    """Command line interpreter for generating UML class diagram"""

    def __init__(self, my_name=">"):
        Cmd.__init__(self, my_name)
        self.my_name = my_name
        self.prompt = ">>" + my_name + ">> "
        self.file_to_data = FileToData()

    def do_pyr_class_diagram(self, file_names):
        """Generate a class diagram in png format from given [png_file_name_suffix py_file_name.py]"""
        self.file_names = file_names
        pyreverse_command = 'pyreverse -ASmn -o png -p ' + file_names
        subprocess.call(pyreverse_command)
        print(file_names + ' are done')

    def help_pyr_class_diagram(self):
        print("\n".join(['Generate a class diagram in png format from given file',
                         'class diagram [output png file name suffix] [input source code file name.py])']))

    def do_readsourcefile(self, file_name):
        """This function is incomplete. Harry is still working on this"""
        self.file_to_data.readfile(file_name)
        print("The ast nodes below has been read from the given file:")
        self.file_to_data.show_ast_nodes()

    def do_displaysourcefilenodes(self, file_name):
        """error is given. This function is incomplete. Harry is still working on this"""
        self.file_to_data.show_ast_nodes()

    def do_displayallclasses(self, file_name):
        """error is given. This function is incomplete. Harry is still working on this"""
        self.file_to_data.readfile(file_name)
        self.file_to_data.show_all_classes()

    def do_dot_2_png(self, input_dot_file_name):
        # self.file_names = file_name
        # url = "http://docs.python.org/library/webbrowser.html"
        # chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        dot_command = 'dot -Tpng ' + input_dot_file_name + ' -o ' + input_dot_file_name + '.png'
        subprocess.call(dot_command)
        print(input_dot_file_name + '.png ' + ' are done')

    def do_quit(self, line):
        """Exit this command line interpreter"""
        print("Quitting......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from this CLI', ':return: True']))


if __name__ == '__main__':
    my_cli = MyCli()
    my_cli.cmdloop()
