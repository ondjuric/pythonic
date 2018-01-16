__author__ = 'ondjuric'
# Blackjack
# From 1 to 7 players compete against a dealer

import cards, games


class BJCard(cards.PositionableCard):
    """ A Blackjack Card. """

    ACE_VALUE = 1

    def get_value(self):
        if self.is_face_up:
            value = BJCard.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
        else:
            value = None
        
        return value

    value = property(get_value)


class BJDeck(cards.Deck):
    """ A BlackJack Deck. """

    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))


class BJHand(cards.Hand):
    """ A BlackJack Hand. """

    def __init__(self, name):
        super(BJHand, self).__init__()
        # hand owner
        self.name = name
    
    def __str__(self):
        rep = self.name + ":\t" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    def get_total(self):
        
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
        # add up card values, treat each Ace as 1
        total = 0
        for card in self.cards:
            total += card.value
        
        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE:
                contains_ace = True
        
        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and total <= 11:
            # add only 10 since we've added 1 for the Ace
            total += 10
        
        return total

    # IMHO the best thing in Python, mighty property!
    total = property(get_total)

    def is_busted(self):
        return self.total > 21


class BJPlayer(BJHand):
    """ A BlackJack Player. """

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, " busts!")
        self.lose()

    def lose(self):
        print(self.name, " loses. :(")
    
    def win(self):
        print(self.name, " wins. :)")
    
    def push(self):
        print(self.name, " pushes. :D")


class BJDealer(BJHand):
    """ A BlackJack Dealer. """
    
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, " busts.")
    
    def flip_first_card(self):
        first_card = self.cards[0]
        print("-----", type(first_card))
        first_card.flip()


class BJGame(object):
    """ A BlackJack Game. """

    def __init__(self, names):
        self.players = []
        self.players = [BJPlayer(name) for name in names]

        self.dealer = BJDealer("Dealer")

        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()
    
    def get_still_playing(self):
        remaining = []
        for player in self.players:
            if not player.is_busted():
                remaining.append(player)
        
        return remaining

    # list of players still playing (not busted) this round
    still_playing = property(get_still_playing)

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    
    def play(self):
        
        # deal initial two cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card() # hide dealer's first card
        
        for player in self.players:
            print(player)
        
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)
        
        self.dealer.flip_first_card() # reveal dealer's first

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)
        
        if self.dealer.is_busted():
            # everyone still playing wins
            for player in self.still_playing:
                player.win()
        else:
            # compare each player still playing to dealer
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()
        
        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWelcome to BlackJack!\n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Enter player's name: ")
        names.append(name)
    print("----Creating the game----")

    game = BJGame(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again? (Y/N): ")

main()
input("\n\nPress the enter key to exit.")
