class Dog:
    def __init__(self, name='Kermit'):
        self.__name = name
        self.__age = 13

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Dog: Name:{self.__name} Age:{self.__age}"

    def set_name(self, name):
        self.__name = name
