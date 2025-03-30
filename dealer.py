from deck import Deck

class Dealer:
    def __init__(self, game_deck: Deck):
        self.game_deck = game_deck
        self.dealer_hand = list()
        self.dealer_score = 0
        self.ace_count = 0
        self.is_sitting = True

    def draw_card(self):
        return self.game_deck.deck.pop()

    def get_score(self):
        for card in self.dealer_hand:
            self.dealer_score += card.rank.value

        while self.dealer_score > 21 and self.ace_count > 0:
            self.dealer_score -= 10
            self.ace_count -= 1

        return self.dealer_score