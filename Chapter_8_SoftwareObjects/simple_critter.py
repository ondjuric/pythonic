__author__ = 'olgica'
# Simple Critter
# Demonstrates a basic class and object, creating and accessing object attributes


class Critter(object):
    """
    A virtual pet.
    """
    def __init__(self, name):
        print 'A new critter has been born!'
        self.name = name

    def __str__(self):
        rep = 'Critter object\n'
        rep += 'name: ' + self.name + '\n'
        return rep

    def talk(self):
        print 'Hi! I am ', self.name, '\n'


# main
crit1 = Critter('Leo')
crit1.talk()

crit2 = Critter('Boki')
crit2.talk()

print 'Printing crit1'
print crit1

print 'Directly accessubg crit1.name: '
print crit1.name


raw_input('\nPress the Enter key to Exit!')