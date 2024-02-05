# property decorator practice
# so here we have made getter and setter and deleter


# decorator to check the type of argument
def type_checker(*arg_types):
    def decorator(func):
        def wrapper(*args):
            if all(isinstance(arg, arg_type) for arg, arg_type in zip(args[1:], arg_types)):
                return func(*args)
            else:
                raise TypeError("Type of argument provided is wrong")
        return wrapper
    return decorator


class Person:

    @type_checker(str, str, int)
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @type_checker(str)
    @fullname.setter
    def change_name(self, name):
        self.first, self.last = name.split(" ")
        return self.first, self.last

    @type_checker(str)
    @fullname.setter
    def change_first(self, f):
        self.first = f
        return self.first

    @type_checker(str)
    @fullname.setter
    def change_last(self, l):
        self.last = l
        return self.last

    @fullname.deleter
    def deleting_name(self):
        self.first = self.last = None
        return None, None

    @property
    def is_adult(self):
        return self.age >= 18

    @type_checker(int)
    @is_adult.setter
    def change_age(self, age):
        self.age = age
        return self.age

p = Person("anjali", "sharma", 50)
print(p.fullname)
p.change_name = "xxx sharma"
print(p.fullname)
print(p.is_adult)
print(p.deleting_name)
