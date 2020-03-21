from cmd import Cmd
import subprocess
from file_to_data import FileToData
import os.path
from os import path
import webbrowser
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class MyCli(Cmd):
    """Command line interpreter for generating UML class diagram"""

    # Harry's work
    def __init__(self, my_name=">"):
        Cmd.__init__(self, my_name)
        self.my_name = my_name
        self.prompt = ">>" + my_name + ">> "
        self.file_to_data = FileToData()

    # Harry's work
    def do_pyr_class_diagram(self, file_names):
        """Generate a class diagram in png format from given [png_file_name_suffix py_file_name.py]"""
        self.file_names = file_names
        python_file_name = file_names[(file_names.find(" ")+1):]
        png_file_name = 'classes_' + file_names[0:(file_names.find(" "))] +'.png'
        try:
            if path.exists(python_file_name):
                pyreverse_command = 'pyreverse -ASmn -o png -p ' + file_names
                subprocess.call(pyreverse_command)
                print(file_names + ' are done')
                #show png image
                img = mpimg.imread(png_file_name)
                fig = plt.imshow(img)
                fig.axes.get_xaxis().set_visible(False)
                fig.axes.get_yaxis().set_visible(False)
                plt.show()

            else:
                print("Your given python file does not exist in the current directory "
                      "or your input arguments were wrong. The input arguments "
                      "should be [png_file_name_suffix py_file_name.py]. "
                      "Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def help_pyr_class_diagram(self):
        print("\n".join(['Generate a class diagram in png format from a given python file',
                         'Syntax: pyr_class_diagram [output png file name suffix] '
                         '[input source code file name.py])']))

    # Harry's work
    def do_read_source_file(self, file_name):
        """This function extract data from the given python file to be an ast node.
        The file name should be [py_file_name.py]. The node will display as an indication of extraction"""
        try:
            if path.exists(file_name):
                self.file_to_data.read_file(file_name)
                print("The ast nodes below has been read from the given python file, " + file_name + ":")
                self.file_to_data.show_ast_nodes()
            else:
                print("Your given python file does not exist in the current directory ")
                print("or your input arguments were wrong. The input arguments ")
                print("should be [py_file_name.py]. ")
                print("Please try again!")
        except Exception as err:
            print("Please try again! The exception is: ", err)

    # Harry's work
    def help_read_source_file(self):
        print("\n".join(['Extract data from the given python file to be an ast node',
                         'Syntax: read_source_file [input source code file name.py]']))


    def do_displaysourcefilenodes(self, file_name):
        """error is given. This function is incomplete. Harry is still working on this"""
        self.file_to_data.show_ast_nodes()

    def do_displayallclasses(self, file_name):
        """error is given. This function is incomplete. Harry is still working on this"""
        self.file_to_data.read_file(file_name)
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
