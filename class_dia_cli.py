from my_cli import MyCli
import argparse
import webbrowser
import sys

def run(args):
    my_cli = MyCli(args.letter)
    my_cli.cmdloop()

def main():
    parser = argparse.ArgumentParser(description="This is a program going to a CLI to generate UML class diagram from Source Codes")
    parser.add_argument("-l", help="optional: give a letter displaced at the beginning of each command line",
                        dest="letter", type=str, default=">")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()