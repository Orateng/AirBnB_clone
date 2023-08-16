#!/usr/bin/python3
# The modules used for the command interpreter
import cmd
from models.base_model import BaseModel

# The command interpreter is made in HBNBCommand class


class HBNBCommand(cmd.Cmd):
    # The command interpreter is implemented
    prompt = '(hbnb)'

    def help_help(self):
        """
        help command for a documented description
        """
        print("Help command")

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, line):
        # The create function maintain class objects
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in model.storage.classes():
            print("** class doesn't exist **")
        else:
            b = model.storage.classes()[line]()
            b.save()
            print(b.id)

    def emptyline(self):
        """Emptyline method that should not do anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
