import os

class User:
    active_users = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old.."

    def __add__(self, data):
        return f"{self.first_name} {self.last_name} is {self.age} years old.. and likes {data}"

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

class Moderator(User):
    def __init__(self, first_name, last_name, age, community):
        super().__init__(first_name, last_name, age)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.community}"