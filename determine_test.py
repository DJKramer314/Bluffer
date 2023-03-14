from pokergame import PokerGame
from card import Card

# The rankings are as follows, with higher cards being of better rank: \n
#         1: High Card \n
#         2: Pair \n
#         3: Two Pair \n
#         4: Three of a Kind \n
#         5: Straight \n
#         6: Flush \n
#         7: Full House \n
#         8: Four of a Kind \n
#         9: Straight Flush \n
#         10: Royal Flush \n


def test1():
    hand = (Card("2s"), Card("3h"))
    table = ()
    game = PokerGame(hand, table)
    assert game.determine_hand() == 1


def test2():
    hand = (Card("2s"), Card("2h"))
    table = ()
    game = PokerGame(hand, table)
    assert game.determine_hand() == 2


def test3():
    hand = (Card("2s"), Card("2h"))
    table = (Card("3s"), Card("3h"))
    game = PokerGame(hand, table)
    assert game.determine_hand() == 3


def test4():
    hand = (Card("2s"), Card("2h"))
    table = (Card("2d"),)
    game = PokerGame(hand, table)
    assert game.determine_hand() == 4


def test5():
    hand = (Card("2s"), Card("3h"))
    table = (Card("4d"), Card("5h"), Card("6c"))
    game = PokerGame(hand, table)
    assert game.determine_hand() == 5


def test6():
    hand = (Card("2h"), Card("4h"))
    table = (Card("6h"), Card("8h"), Card("10h"))
    game = PokerGame(hand, table)
    assert game.determine_hand() == 6


def test7():
    hand = (Card("2h"), Card("2s"))
    table = (Card("3d"), Card("3s"), Card("3h"))
    game = PokerGame(hand, table)
    assert game.determine_hand() == 7


def test8():
    hand = (Card("2h"), Card("2s"))
    table = (Card("2d"), Card("2c"))
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test9():
    hand = (Card("2h"), Card("3h"))
    table = (Card("4h"), Card("5h"), Card("6h"))
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test10():
    hand = (Card("10h"), Card("Jh"))
    table = (Card("Qh"), Card("Kh"), Card("Ah"))
    game = PokerGame(hand, table)
    assert game.determine_hand() == 10
