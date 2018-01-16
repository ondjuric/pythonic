__author__ = 'olgica'
# Property Critter
# Demonstrates get and set methods and properties


class Critter(object):
    """
    A virtual pet.
    """
    def __init__(self, name):
        print('A new Critter has been born!')
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name == "":
            print('\nCritter has to have a name.')
        else:
            self.__name = new_name
            print('Name changed successful.')

    # property essentially wraps access methods around the consistent and familiar dot notation.
    name = property(get_name, set_name)

    def talk(self):
        print('\nHi, I am ', self.name)


# main
crit1 = Critter('Leo')
crit1.talk()

crit1.set_name("")
crit1.name = 'Kleo'
crit1.talk()

input('Enter Key to Exit!')