from pokergame import PokerGame
from card import Card
from deck import Deck


table = (Card(5, "Hearts"),
         Card(5, "Hearts"),
         Card(5, "Hearts"),
         Card(5, "Hearts"))

hand = (Card(5, "Hearts"), Card(5, "Hearts"))

game = PokerGame(hand, table)
print(game.calculate_winning_odds())
