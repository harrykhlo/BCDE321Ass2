from cmd import Cmd
from Diagram import DiagramCreator
import pickle


class MyPrompt(Cmd):
    prompt = '> '
    intro = "Type ? to list commands"  # actually do this

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

    def do_pickle(self, inp):  # make a py file for pickle
        DiagramCreator.MyCreator('PickleDot.dot', inp).create_diagram()  # change so file can be anything instead of just dot
        pickle_file = open(input('Enter filename: '), 'wb')
        pickle.dump('classes.PickleDot.dot', pickle_file)  # remove classes
        pickle_file.close()

    def help_pickle(self):
        print('a')

    def do_unpickle(self, inp):  # I will make pickle and unpickle into functions in a new file
        pickle_file = open(inp, 'rb')
        load_file = pickle.load(pickle_file)
        print(load_file)
        pickle_file.close()

    def help_unpickle(self):
        print('b')

    def default(self, inp):
        print(inp + ' is an incorrect command. Type ? to list commands.')

    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    MyPrompt().cmdloop()
