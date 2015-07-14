__author__ = 'olgica'
# Alien Blaster
# Demonstrates object interaction


class Player(object):
    """
    A player in a shooter game.
    """
    def blast(self, enemy):
        print 'The player blasts an enemy.\n'
        enemy.die()


class Alien(object):
    """
    An alien in a shooter game.
    """
    def die(self):
        print "The alien gasps and says: 'Oh, this is it! You killed me!'"


# main
print '\t\tDeath of an Alien\n'

hero = Player()
invader = Alien()
hero.blast(invader)

raw_input('Enter Key to exit!')