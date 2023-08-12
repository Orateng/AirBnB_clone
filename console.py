#!/usr/bin/python3
# The modules used for the command interpreter
import cmd
# from models.base_model import BaseModel
# from models import storage
# The command interpreter is made in HBNBCommand class


class HBNBCommand(cmd.Cmd):
    # The command interpreter is implemented
    prompt = '(hbnb)'

    """
    The help function for the command
    interpreter HBNBCommand class
    """
    def help_help(self):
        """
        help command for a documented description
        """
        print("Help command")

    """
    The EOF function in implemented
    for HBNBCommand class
    """
    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    """
    The quit function is implemented for
    HBNBCommand class
    """
    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    """
    The create funtion is implemented for
    HBNBCommand class
    """
    def do_create(self, line):
        # The create function maintain class objects
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
