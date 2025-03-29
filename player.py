from card import Card


class Player:
    #todo implement money value for player
    def __init__(self):
        self.player_hand = list()
        self.hand_value  = 0
        self.ace_count   = 0
        self.is_sitting  = True

    #todo money logic method to add bet amounts
    def place_bet(self):
        pass

    #todo money logic method for clearing bet amounts
    def clear_bet(self):
        pass

    def stand(self):
        self.is_sitting = False

    def hit(self, card: Card):
        self.player_hand.append(card)

        if card.rank == "ACE":
            self.ace_count += 1

    def get_hand_value(self):
        for card in self.player_hand:
            self.hand_value += card.value

        while self.hand_value > 21 and self.ace_count > 0:
            self.hand_value -= 10
            self.ace_count -= 1

        return self.hand_value