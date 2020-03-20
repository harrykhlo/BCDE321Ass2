from cmd import Cmd
from Diagram import DiagramCreator
from Diagram import PickleMaker


class MyPrompt(Cmd):
    prompt = '> '
    intro = "Type ? to list commands"

    def do_exit(self, inp):
        # exit the application.
        print('Exiting Program...')
        return True

    def help_exit(self):
        print('Exit the application.')

    def do_diagram(self, inp):
        image_name = input('Image name/type:')
        DiagramCreator.MyCreator(image_name, inp).create_diagram()

    def help_diagram(self):
        print('Create a class diagram. Enter file location of py/dot file, then enter name/type of image.')

    def do_pickle(self, inp):
        PickleMaker.MyPickle(inp, input('name of pickle file: ')).make_pickle()

    def help_pickle(self):
        print('pickle [filename], enter file to pickle then the name of the pickle file')

    def do_unpickle(self, inp):  # i don't know if this is correct or not
        PickleMaker.MyPickle('a', inp).make_pickle()
        """pickle_file = open(inp, 'rb')  # https://www.datacamp.com/community/tutorials/pickle-python-tutorial
        load_file = pickle.load(pickle_file)
        print(load_file)
        pickle_file.close()"""

    def help_unpickle(self):
        print('unpickle [picklefilename], enter the name of a file that has been pickled')

    def do_db(self):
        pass

    def help_db(self):
        print('a')

    def default(self, inp):
        print(inp + ' is an incorrect command. Type ? to list commands.')

    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    MyPrompt().cmdloop()
