#!/usr/bin/python3
"""import module cmd"""
import cmd
"""define class"""

class HBNBCommand(cmd.Cmd):
    """assign value to prompt"""
    prompt = '(hbnb) '

    def please_quit(self, args):
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    def do_create(self, args):
        """creating new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        argss = args.split()
        class_name = argss[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """print string rep. of instance"""
        if not args:
            print("** class name missing **")
            return
        argss = arg.split()
        class_instance = argss[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(argss) < 2:
            print("** instance id is missing **")
            return
        instance_id = argss[1]
        key = "{}.{}".format(class_name,instance_id)
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
            """print string rep of all instances"""
            argss = args.split()
            if not args or argss[0] in self.valid_classes:
                instance_list = []
                for key, value in models.storage.all().items():
                    if not args or value.__class__.__name__ == argss[0]:
                        instance_list.append(str(value))
                        print(instance_list)
                    else:
                        print("** class doesn't exist **")
    def all_update(self, args):
        """update an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        argss = args.split()
        class_name = argss[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

            if len(argss) < 2:
                print("** instance id missing **")
                return

            instance_id = argss[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if len(argss) < 3:
                print("** attribute name missing **")
                return
            if len(argss) < 4:
                print("** value missing **")
                return

