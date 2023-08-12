#!/usr/bin/python3
"""Create a Console app"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Define a command line object"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Indicate the end of the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
