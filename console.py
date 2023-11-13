#!/usr/bin/python3
"""import module cmd"""
import cmd
import uuid
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage
"""define class"""

class HBNBCommand(cmd.Cmd):
    """assign value to prompt"""
    prompt = '(hbnb) '
    class_list = {"BaseModel": BaseModel}, {"User": User}, {"State": State}, {"City": City}, {"Amenity": Amenity}, {"Place": Place}, {"Review": Review}

    def do_quit(self, args):
        """Exit program"""
        print("Exiting...!")
        return True

    def do_EOF(self, args):
        """Exit program"""
        print("\nExiting...!")
        return True

    def empty_line(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, args):
        """creating new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif args != "BaseModel" and args != "User":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            
    def do_show(self, args):
        """Prints the string representation of an instance"""
        argss = args.split()
        if not args:
            print("** class name missing **")
        elif argss[0] != "BaseModel" and argss[0] != "User":
            print("** class doesn't exist **")
        elif len(argss) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argss[0], argss[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")


    def do_destroy(self, args):
        """Deletes an instance based on the class name"""
        argss = args.split()
        if not args:
            print("** class name missing **")
        elif argss[0] != "BaseModel" and argss[0] != "User":
            print("** class doesn't exist **")
        elif len(argss) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argss[0], argss[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        words = arg.split()
        if len(words) > 0:
            class_name = words[0]
            try:
                model_class = globals()[class_name]
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            class_name = None
        all_list = []
        for key, val in storage.all().items():
            if class_name is None or isinstance(val, model_class):
                all_list.append(val.__str__())
        print(all_list)
    
    def do_update(self, args):
        """update an instance based on the class name and id"""
        argss = args.split()
        if not args:
            print("** class name missing **")
        elif argss[0] != "BaseModel" and argss[0] != "User":
            print("** class doesn't exist **")
        elif len(argss) < 2:
            print("** instance id missing **")
        elif len(argss) < 3:
            print("** attribute name missing **")
        elif len(argss) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(argss[0], argss[1])
            if key in storage.all():
                setattr(storage.all()[key], argss[2], argss[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
