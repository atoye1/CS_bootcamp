#!python3

class Person:
    def __init__(self):
        self.__age =0

    def get_age(self):
        return self.__age

    def set_age(self,value):
        self.__age = value


class Person_p:
    def __init__(self):
        self.__age= 0
        self.__my_key=1

    @property
    def my_key(self):
        return self.__my_key

    @my_key.setter
    def my_key(self,value):
        self.__my_key = value

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        self.__age = value
