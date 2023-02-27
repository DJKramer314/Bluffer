from pokergame import PokerGame
from card import Card
from deck import Deck


table = (Card("Hearts", 5),
         Card("Hearts", 5),
         Card("Hearts", 5),
         Card("Hearts", 5))

hand = (Card("Hearts", 5), Card("Hearts", 5))

game = PokerGame(hand, table)
