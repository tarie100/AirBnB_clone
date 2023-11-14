#!/usr/bin/python3
"""import module cmd"""
import cmd
import uuid
import re
from shlex import split
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
        if class_name and hasattr(model_class, 'all'):
            all_list = [str(instance) for instance in model_class.all()]

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

    def do_count(self, arg):
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def exec_cls_cmd(self, class_name, arg):
        if arg[:6] == ".all()":
            self.do_all(class_name)
        elif arg[:8] == ".count()":
            self.do_count(class_name)
        elif arg[:6] == '.show(':
            self.do_show(class_name + ' ' + arg[7:-2])
        elif arg[:9] == '.destroy(':
            self.do_destroy(class_name + ' ' + arg[10:-2])
        else:
            print("Not a valid command")

    def do_BaseModel(self, arg):
        self.exec_cls_cmd('BaseModel', arg)

    def do_User(self, arg):
        self.exec_cls_cmd('User', arg)

    def do_State(self, arg):
        self.exec_cls_cmd('State', arg)

    def do_City(self, arg):
        self.exec_cls_cmd('City', arg)

    def do_Place(self, arg):
        self.exec_cls_cmd('Place', arg)

    def do_Amenity(self, arg):
        self.exec_cls_cmd('Amenity', arg)
    def do_Review(self, arg):
        self.exec_cls_cmd('Review', arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
