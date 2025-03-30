import card
import random

def _create_deck():
    deck = list()

    for suit in card.Suit:
        for rank in card.Rank:
            deck.append(card.Card(rank, suit))

    return deck

class Deck:
    def __init__(self):
        self.deck = _create_deck()
        random.shuffle(self.deck)


