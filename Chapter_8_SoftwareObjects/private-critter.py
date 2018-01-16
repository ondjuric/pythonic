__author__ = 'olgica'
# Private Critter
# Demonstrates private variables and methods


class Critter(object):
    """
    A virtual pet.
    """
    def __init__(self, name, mood):
        print('A new critter has been born!')
        self.name = name  # public attribute
        self.__mood = mood  # private attribute

    def talk(self):
        print('\nI am ', self.name)
        print('Right now I feel', self.__mood, '\n')

    def __private_method(self):
        print('This is private method')

    def public_method(self):
        print('This is public method')
        self.__private_method()  # access to private method within public one


# main
crit1 = Critter('Leo', 'happy')
crit1.talk()
crit1.public_method()

input('Enter key to Exit')