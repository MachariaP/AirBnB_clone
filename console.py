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
            dee = split(arg[:brackets.span()[0]])
            patl = [i.strip(",") for i in dee]
            patl.append(brackets.group())
            return patl
    else:
        dee = split(arg[:curly_braces.span()[0]])
        patl = [i.strip(",") for i in dee]
        patl.append(curly_braces.group())
        return patl


class HBNBCommand(cmd.Cmd):
    """Defines the Holberton command line interpreter(hbnb)"""

    prompt = "(hbnb)"
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    # Override cmdloop to intercept empty line inputs
    def cmdloop(self, intro=None):
        """Repeatedly issue a prompt, accept input, parse an initial prefix
        off the received input, and dispatch to action methods, passing them
        the remainder of the line as argument.
        """
        while not self.quit:
            try:
                line = input(self.prompt)
                if line.strip() == "":
                    print("Empty line detected. Nothing will be executed.")
                    continue  # Skip further processing for empty lines
                else:
                    self.onecmd(line)
            except KeyboardInterrupt:
                print("^C")
                self.quit = True
            except Exception as e:
                print(e)
                self.quit = True

    def do_nothing(self, arg):
        """function does nothing"""

        pass

    def do_quit(self, arg):
        """this function exits the program """

        return True

    def do_EOF(self, arg):
        """handles the EOF character"""

        print()
        return True

    def do_create(self, arg):
        """This creates an instance and print id"""

        my_arg = parse(arg)
        if len(my_arg) == 0:
            print("** class name missing **")
        elif my_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(my_arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """ method that display string representation of
        class instance of a certain id"""

        my_arg = parse(arg)
        objdict = storage.all()
        if len(my_arg) == 0:
            print("** class name missing **")
        elif my_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(my_arg[0], my_arg[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(my_arg[0], my_arg[1])])

    def do_destroy(self, arg):
        """This prints all string representation of all instances.
        """

        my_arg = parse(arg)
        obj_dic = storage.all()
        if len(my_arg) == 0:
            print("** class name missing **")
        elif my_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(my_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(my_arg[0], my_arg[1]) not in obj_dic.keys():
            print("** no instance found **")
        else:
            del obj_dic["{}.{}".format(my_arg[0], my_arg[1])]
            storage.save()

    def do_all(self, arg):
        """This prints all string representation of all instances.
        """

        my_arg = parse(arg)
        if len(my_arg) > 0 and my_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obje = []
            for obj in storage.all().values():
                if len(my_arg) > 0 and my_arg[0] == obj.__class__.__name__:
                    obje.append(obj.__str__())
                elif len(my_arg) == 0:
                    obje.append(obj.__str__())
            print(obje)

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
            print("** attribute name missing **")
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
