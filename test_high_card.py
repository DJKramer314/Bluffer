from pokergame import PokerGame
from card import Card


def test1():
    hand = (Card("2s"), Card("2h"))
    table = ()
    game = PokerGame(hand, table)
    assert game.determine_hand() == 1

# Ensure that the hand has:
# - No duplicate numbers
# - No straights
# - No flushes
