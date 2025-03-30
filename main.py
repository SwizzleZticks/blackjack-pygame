from dealer import Dealer
from deck import Deck
from player import Player


def main():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player()
    player.hit(dealer.draw_card())

    print(player.get_score())

main()