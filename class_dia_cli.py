from my_cli import MyCli
import argparse
import webbrowser
import sys


# Harry's work
def run(args):
    my_cli = MyCli(args.letter[0])
    try:
        my_cli.cmdloop()
    except Exception as err:
        print("Please try again! The exception is: ", err)


# Harry's work
def main():
    parser = argparse.ArgumentParser(description=
                                     "This is a program going to a CLI to generate " +
                                     "UML class diagram from Source Codes")
    parser.add_argument("-l", help="optional: give a letter displaced at the beginning of each " +
                                   "command line. If user enter a string, only first character " +
                                   "will be shown.", dest="letter", type=str, default=">")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


# Harry's work
if __name__ == '__main__':
    main()
