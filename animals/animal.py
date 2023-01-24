class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.__name = value