class Person:
    def __init__(self, name='Tal', age=20):
        self.__name = name
        self.__age = age

    def say(self):
        print('Hi :')

    def __str__(self):
        return f"Person {self.__name} is {self.__age} years old"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
