__author__ = 'ondjuric'
# Playing Cards 3.0
# Demonstrates inheritance - overriding methods


class Card(object):
    """
    Represents a playing card.
    """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        rep = self.rank + self.suit
        return rep


class UnprintableCard(Card):
    """
    Represents a card that won't reveal its rank or suit when printed.
    """

    def __str__(self):
        return "<unprintable>"


class PositionableCard(Card):
    """
    Represents a card that can be face up or face down.
    """
    
    def __init__(self, rank, suit, face_up=True):
        # 1st arg: wakes its superclass;
        # 2nd arg: reference to new instance of PC class, so that superclass can get at the object to add its attributes;
        # super's __init__ tell that we want to invoke the constructor method of superclass and want to pass it the values of rank and suit;
        super(PositionableCard, self).__init__(rank, suit)
        self.is_face_up = face_up
    
    def __str__(self):
        # overrides a method inherited from superclass and invokes the overridden method
        if self.is_face_up:
            rep = super(PositionableCard, self).__str__()
        else:
            rep = "XX"
        
        return rep

    def flip(self):
        """ Flips a card over by toggling the value of an object's face_up attribute. """
        self.is_face_up = not self.is_face_up


class Hand(object):
    """
    A hand of playing cards
    """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for cards in self.cards:
                rep += str(cards) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """
    A deck of playing cards.
    """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Cannot continue deal. Out of cards.')


if __name__ == '__main__':
    print("This is a module with classes for playing cards.")
    input("\n\nPress the enter key to exit.")
