import os
import cmd
import subprocess
import shlex
import sys


class Cli(cmd.Cmd, object):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "
        self.intro = "Welcome to commands!"
        self.__setCanExit(True)
        
    def __canExit(self):
        return self.canExit
    
    def __setCanExit(self, value):
        self.canExit = value

    def preloop(self):
        """Initialization"""
        cmd.Cmd.preloop(self)   # sets up command completion
        self._hist = []      # No history yet
        self._locals = {}      # Initialize execution namespace for user
        self._globals = {}

    def postloop(self):
        """Finish up everything"""
        cmd.Cmd.postloop(self)   # Clean up command completion
        print("The application will now exit!")
        
    def emptyline(self):    
        """Do nothing on empty input line"""
        pass

    # The do's
    def do_exit(self, args):
        """Exits from the console"""
        if self.__canExit(): return True
        print ("Please, wait until all operations end")
        return False

    # Command definitions to support Cmd object functionality ##
    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(args)

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

    def do_help(self, args):
        """Get help on commands"""
        cmd.Cmd.do_help(self, args)

    def do_create(self, file_name):
        """Create UML class diagram"""
        command = 'pyreverse -o png -ASmy -k {0} -p class'.format(file_name)
        subprocess.call(shlex.split(command))

    def run_pyreverse(self):
        """run pyreverse"""
        from pylint.pyreverse.main import Run
        Run(sys.argv[1:])


if __name__ == '__main__':
    console = Cli()
    console . cmdloop() 

