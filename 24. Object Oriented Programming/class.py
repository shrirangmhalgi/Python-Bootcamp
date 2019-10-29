# _var_name -> private variable made for internal use
# __var_name__ -> dunder methods these are special methods which is used to override the inbuild methods also known as magic methods
# __var_name -> it is used for name mingling (_User__var_name) it is used in inheritance...

# we use camelcase to name a class and is singular

class User:
    active_users = 0 # this is a class attribute... just like a static variable

    # __init__ is like a constructor
    # self is a keyword which is similar to "this" keyword
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1
    
    # it is like the toString method which represents the object...
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old.."

    def __add__(self, data):
        return f"{self.first_name} {self.last_name} is {self.age} years old.. and likes {data}"

    # Using class method the whole class is passed as a reference Make it a class method when you are working with class and not the instance
    @classmethod
    def get_active_users(cls):
        return cls.active_users

    @classmethod
    def create_user(cls, data_string):
        first_name, last_name, age = data_string.split(",")
        return cls(first_name, last_name, age)

    def full_name(self):
        return f"My full name is {self.first_name.upper()} {self.last_name.upper()} :) "

    def initials(self):
        return f"{self.first_name[0].upper()}.{self.last_name[0].upper()}."

    def is_senior(self):
        if self.age >= 65:
            return True
        return False

user = User("shrirang", "mhalgi", 21)
print(user.full_name())
print(user.initials())
print(User.active_users)
print(User.get_active_users())
u = User.create_user("Tom,Jones,78")
print(u.first_name)
print(u.full_name())
print(u.__repr__())
print(u.__add__("Ice Cream"))
print(u.__repr__())