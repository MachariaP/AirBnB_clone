#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the Holberton command line interpreter(hbnb)"""

    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_nothing(self, arg):
        """function that does nothing"""
        pass

    def do_quit(self, arg):
        """function that exists the program and saves data"""
        return True

    def do_EOF(self, arg):
        """signal to close the program"""
        print("")
        return True

    def do_create(self, arg):
        """
        method that creates a new class instance
        and print id.
        """
        arg2 = parse(arg)
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg2[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        method that isplay string representation of a
        class instance of a certain id.
        """
        arg2 = parse(arg)
        objdict = storage.all()
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg2) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg2[0], arg2[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg2[0], arg2[1])])

    def do_destroy(self, arg):
        """
        method that delete a class
        instance of a given id.
        """
        arg2 = parse(arg)
        objdict = storage.all()
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg2) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg2[0], arg2[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg2[0], arg2[1])]
            storage.save()

    def do_all(self, arg):
        """
        method that displays string representations of all
        instances of a class.
        nb:If no class is specified, then
        display all instantiated objects.
        """
        arg2 = parse(arg)
        if len(arg2) > 0 and arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj2 = []
            for obj in storage.all().values():
                if len(arg2) > 0 and arg2[0] == obj.__class__.__name__:
                    obj2.append(obj.__str__())
                elif len(arg2) == 0:
                    obj2.append(obj.__str__())
            print(obj2)

    def do_count(self, arg):
        """
        method that retrieve the number of
        instances of a specified class.
        """
        arg2 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg2[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Update a class instance of a given id by adding attributes
        ."""
        arg2 = parse(arg)
        objdict = storage.all()

        if len(arg2) == 0:
            print("** class name missing **")
            return False
        if arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg2) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg2[0], arg2[1]) not in objdict.keys():
            print("** no istance found **")
            return False
        if len(arg2) == 2:
            print("** sttribute name missing **")
            return False
        if len(arg2) == 3:
            try:
                type(eval(arg2[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg2) == 4:
            obj = objdict["{}.{}".format(arg2[0], arg2[1])]
            if arg2[2] in obj.__class__.__dict__.keys():
                valueType = type(obj.__class__.__dict__[arg2[2]])
                obj.__dict__[arg2[2]] = valueType(arg2[3])
            else:
                obj.__dict__[arg2[2]] = arg2[3]
        elif type(eval(arg2[2])) == dict:
            obj = objdict["{}.{}".format(arg2[0], arg2[1])]
            for i, j in eval(arg2[2]).items():
                if (i in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[i]) in {str, int, float}):
                    valueType = type(obj.__class__.__dict__[i])
                    obj.__dict__[i] = valueType(j)
                else:
                    obj.__dict__[i] = j
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
