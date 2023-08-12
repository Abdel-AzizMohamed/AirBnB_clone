#!/usr/bin/python3
"""Create a Console app"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Define a command line object"""
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User}

    def emptyline(self):
        """Do nothing in empty line input."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Indicate the end of the program"""
        return True

    def do_create(self, line):
        """Create a new instance"""
        if line == "":
            print("** class name missing **")
        elif line in self.classes:
            obj = self.classes[line]()
            models.storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")
        
    def do_show(self, line):
        """Prints the string representation of an instance"""

        line_split = line.split(" ")

        if line == "":
            print("** class name missing **")
        elif line_split[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        else:
            data = models.storage.all()
            obj_key = "{}.{}".format(line_split[0], line_split[1])

            if obj_key in data:
                print(data[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance"""

        line_split = line.split(" ")

        if line == "":
            print("** class name missing **")
        elif line_split[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        else:
            data = models.storage.all()
            obj_key = "{}.{}".format(line_split[0], line_split[1])

            if obj_key in data:
                del models.storage._FileStorage__objects[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")


    def do_all(self, line):
        """
            Prints all string representation of all
            instances based or not on the class name
        """
        data = models.storage.all()
        objects = []

        if line == "":
            for value in data.values():
                objects.append(value)
            print(objects)
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in data.items():
                if line in key:
                    objects.append(value)
                print(objects)
            

    def do_update(self, line):
        """Deletes an instance"""

        line_split = line.split(" ")

        if line == "":
            print("** class name missing **")
        elif line_split[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(line_split) == 1:
            print("** instance id missing **")
        else:
            data = models.storage.all()
            obj_key = "{}.{}".format(line_split[0], line_split[1])

            if obj_key not in data:
                print("** no instance found **")
            elif len(line) == 2:
                print("** attribute name missing **")
            elif len(line) == 3:
                print("** value missing **")
            else:
                obj = models.storage._FileStorage__objects[obj_key]
                setattr(obj, line_split[2], line_split[3])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
