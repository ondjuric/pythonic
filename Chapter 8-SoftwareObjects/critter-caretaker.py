__author__ = 'olgica'
# Critter care taker
# A virtual pet to care for


class Critter(object):
    """
    A virtual pet
    """
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = 'Hunger and Boredom\n'
        rep += str(self.hunger) + " " + str(self.boredom)
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __get_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = 'happy'
        elif 5 <= unhappiness <= 10:
            mood = 'okay'
        elif 11 <= unhappiness <= 15:
            mood = 'frustrated'
        else:
            mood = 'mad'
        return mood

    mood = property(__get_mood)

    def talk(self):
        print 'I am', self.name, 'and I feel', self.mood, 'now.\n'
        self.__pass_time()

    def eat(self, food):
        print 'Brrrruuupp! Thank you.'
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print 'Wheeee!'
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
        crit_name = raw_input('What do you want to name your critter?: ')
        crit = Critter(crit_name)

        choice = None
        while choice != '0':
            print """
            Critter Caretaker

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """
            choice = raw_input('Choice: ')

            # exit
            if choice == '0':
                print 'Good-bye.'

            # listen to your critter
            elif choice == '1':
                crit.talk()

            # feed your critter
            elif choice == '2':
                food = int(raw_input('How much food?: '))
                crit.eat(food)

            # play with your critter
            elif choice == '3':
                fun = int(raw_input('How much fun: '))
                crit.play(fun)

            elif choice == '4':
                print crit

            # some unknown choice
            else:
                print '\nSorry, but', choice, 'is not a valid choice.'

# start the program
main()

raw_input('Press the Enter key to Exit.')