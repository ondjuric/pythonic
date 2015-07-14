__author__ = 'olgica'
# Classy Critter
# Demonstrates class attributes and static methods


class Critter(object):
    """
    A virtual pet.
    """
    total = 0

    def status():
        print '\nTotal number of critters is: ', Critter.total

    status = staticmethod(status)

    def __init__(self, name):
        print 'A critter has been born!'
        self.name = name
        Critter.total += 1


# main
print 'Accessing the class attribute Critter.total: '
print Critter.total


print '\nCreating Critters.'
crit1 = Critter('Leo')
crit2 = Critter('Boki')
crit3 = Critter('Dzeki')

Critter.status()

print '\nAccessing the class attribute through an object: '
print crit2.total

raw_input('\n\nPress Enter key to Exit.')