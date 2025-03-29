from enum import Enum

class Rank(Enum):
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9
    TEN   = 10
    JACK  = 10
    QUEEN = 10
    KING  = 10
    ACE   = 11

class Suit(Enum):
    HEARTS   = 0
    DIAMONDS = 1
    SPADES   = 2
    CLUBS    = 3

class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank.name.title()} of {self.suit.name.title()}'