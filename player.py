from card import Card


class Player:
    #todo implement money value for player

    def __init__(self):
        self.hands = [[]]
        self.current_hand = 0
        self.player_score  = [0]
        self.ace_count   = [0]
        self.is_sitting  = [True, True]

    def get_current_hand(self):
        return self.hands[self.current_hand]

    def switch_hands(self):
        if self.current_hand == 0:
            self.current_hand = 1
        else:
            self.current_hand += 1

    #todo money logic method to add bet amounts
    def place_bet(self):
        pass

    #todo money logic method for clearing bet amounts
    def clear_bet(self):
        pass

    def stand(self):
        self.is_sitting[self.current_hand] = False

    def hit(self, card: Card):
        self.hands[self.current_hand].append(card)

        if card.rank == "ACE":
            self.ace_count[self.current_hand] += 1

    #todo implement logic for splitting
    def split(self):
        pass

    #todo implement logic for doubling a bet
    def double(self):
        pass

    def get_score(self):
        for card in self.hands[self.current_hand]:
            self.player_score[self.current_hand] += card.rank.value

        while self.player_score[self.current_hand] > 21 and self.ace_count[self.current_hand] > 0:
            self.player_score[self.current_hand] -= 10
            self.ace_count[self.current_hand] -= 1

        return self.player_score[self.current_hand]