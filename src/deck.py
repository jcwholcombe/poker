#this is the deck
#order = spades, hearts, diamonds, clubs
import random

class deck:
    def __init__(self):
        self.cards = [0] * 52
        self.deck_size = 52
        self.board = [0] * 5
        for i in range(1, 53):
            self.cards[i] = i

    #takes in nothing, removes a random card from the deck and returns that card
    def remove_card(self):
        card_index = random.randint(0, 51)
        card = self.cards[card_index]
        while (card == 0):
            if card_index == 51:
                card_index = 0
                card = self.cards[card_index]
            else:
                card_index += 1
                card = self.cards[card_index]
        self.cards[card_index] = 0
        self.deck_size -= 1
        return card

#the player class, there are two players
class player:
    def __init__(self):
        self.chips = 100

    def deal_cards(self, game_deck):
        self.hand = [game_deck.remove_card(), game_deck.remove_card]

    def remove_chips(self, amount):
        self.chips -= amount

    def add_chips(self, amount):
        self.chips += amount

    def print_cards(self):
        print(self.hand)

class pot:
    def __init__(self, p1, p2, blind):
        self.pot_size = 1
        #the amount needed to have an even pot, if > 0, p1 must put money in, if < 0, p2 must put money in.
        self.call_needed = 1
        self.p1 = p1
        self.p2 = p2
        if (blind > 0):
            self.p1.remove_chips(blind)
        else:
            self.p2.remove_chips(-1 * blind)

    def end(self):
        if self.call_

#the main class that runs the game
class game:
    def __init__(self):
        self.p1 = player()
        self.p2 = player()
        #1 means p1 uses blind, -1 means p2 does blind
        this.blind = 1

    def run_hand(self):
        this.hand = deck()
        self.p1.deal_cards(this.hand)
        self.p2.deal_cards(this.hand)
        this.pot = pot(this.p1, this.p2, this.blind)
        #preflop
        p1.print_cards
        p2.print_cards
        p1bet = input("P1, 1 to call do you want to call (1), raise or fold (0): ")
        if p1bet < 1:
