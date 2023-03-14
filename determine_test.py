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


def test_royal_flush_s():
    hand = (Card("10s"), Card("Js"))
    table = (Card("Qs"), Card("Ks"), Card("As"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 10


def test_royal_flush_d():
    hand = (Card("10d"), Card("Jd"))
    table = (Card("Qd"), Card("Kd"), Card("Ad"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 10


def test_royal_flush_c():
    hand = (Card("10c"), Card("Jc"))
    table = (Card("Qc"), Card("Kc"), Card("Ac"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 10


def test_royal_flush_h():
    hand = (Card("10h"), Card("Jh"))
    table = (Card("Qh"), Card("Kh"), Card("Ah"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 10


def test_straight_flush_s_2_to_6():
    hand = (Card("2s"), Card("3s"))
    table = (Card("4s"), Card("5s"), Card("6s"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_d_2_to_6():
    hand = (Card("2d"), Card("3d"))
    table = (Card("4d"), Card("5d"), Card("6d"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_c_2_to_6():
    hand = (Card("2c"), Card("3c"))
    table = (Card("4c"), Card("5c"), Card("6c"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_h_2_to_6():
    hand = (Card("2h"), Card("3h"))
    table = (Card("4h"), Card("5h"), Card("6h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_s_3_to_7():
    hand = (Card("3s"), Card("4s"))
    table = (Card("5s"), Card("6s"), Card("7s"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_d_3_to_7():
    hand = (Card("3d"), Card("4d"))
    table = (Card("5d"), Card("6d"), Card("7d"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_c_3_to_7():
    hand = (Card("3c"), Card("4c"))
    table = (Card("5c"), Card("6c"), Card("7c"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_h_3_to_7():
    hand = (Card("3h"), Card("4h"))
    table = (Card("5h"), Card("6h"), Card("7h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_s_4_to_8():
    hand = (Card("4s"), Card("5s"))
    table = (Card("6s"), Card("7s"), Card("8s"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_d_4_to_8():
    hand = (Card("4d"), Card("5d"))
    table = (Card("6d"), Card("7d"), Card("8d"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_c_4_to_8():
    hand = (Card("4c"), Card("5c"))
    table = (Card("6c"), Card("7c"), Card("8c"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_h_4_to_8():
    hand = (Card("4h"), Card("5h"))
    table = (Card("6h"), Card("7h"), Card("8h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_s_5_to_9():
    hand = (Card("5s"), Card("6s"))
    table = (Card("7s"), Card("8s"), Card("9s"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_d_5_to_9():
    hand = (Card("5d"), Card("6d"))
    table = (Card("7d"), Card("8d"), Card("9d"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_c_5_to_9():
    hand = (Card("5c"), Card("6c"))
    table = (Card("7c"), Card("8c"), Card("9c"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_h_5_to_9():
    hand = (Card("5h"), Card("6h"))
    table = (Card("7h"), Card("8h"), Card("9h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_s_6_to_10():
    hand = (Card("6s"), Card("7s"))
    table = (Card("8s"), Card("9s"), Card("10s"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_d_6_to_10():
    hand = (Card("6d"), Card("7d"))
    table = (Card("8d"), Card("9d"), Card("10d"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_c_6_to_10():
    hand = (Card("6c"), Card("7c"))
    table = (Card("8c"), Card("9c"), Card("10c"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_h_6_to_10():
    hand = (Card("6h"), Card("7h"))
    table = (Card("8h"), Card("9h"), Card("10h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_s_7_to_11():
    hand = (Card("7s"), Card("8s"))
    table = (Card("9s"), Card("10s"), Card("Js"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_d_7_to_11():
    hand = (Card("7d"), Card("8d"))
    table = (Card("9d"), Card("10d"), Card("Jd"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_c_7_to_11():
    hand = (Card("7c"), Card("8c"))
    table = (Card("9c"), Card("10c"), Card("Jc"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_h_7_to_11():
    hand = (Card("7h"), Card("8h"))
    table = (Card("9h"), Card("10h"), Card("Jh"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_s_8_to_12():
    hand = (Card("8s"), Card("9s"))
    table = (Card("10s"), Card("Js"), Card("Qs"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_d_8_to_12():
    hand = (Card("8d"), Card("9d"))
    table = (Card("10d"), Card("Jd"), Card("Qd"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_c_8_to_12():
    hand = (Card("8c"), Card("9c"))
    table = (Card("10c"), Card("Jc"), Card("Qc"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_straight_flush_h_8_to_12():
    hand = (Card("8h"), Card("9h"))
    table = (Card("10h"), Card("Jh"), Card("Qh"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 9


def test_four_of_a_kind_2():
    hand = (Card("2s"), Card("2d"))
    table = (Card("2c"), Card("2h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_3():
    hand = (Card("3s"), Card("3d"))
    table = (Card("3c"), Card("3h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_4():
    hand = (Card("4s"), Card("4d"))
    table = (Card("4c"), Card("4h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_5():
    hand = (Card("5s"), Card("5d"))
    table = (Card("5c"), Card("5h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_6():
    hand = (Card("6s"), Card("6d"))
    table = (Card("6c"), Card("6h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_7():
    hand = (Card("7s"), Card("7d"))
    table = (Card("7c"), Card("7h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_8():
    hand = (Card("8s"), Card("8d"))
    table = (Card("8c"), Card("8h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_9():
    hand = (Card("9s"), Card("9d"))
    table = (Card("9c"), Card("9h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_10():
    hand = (Card("10s"), Card("10d"))
    table = (Card("10c"), Card("10h"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_J():
    hand = (Card("Js"), Card("Jd"))
    table = (Card("Jc"), Card("Jh"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_Q():
    hand = (Card("Qs"), Card("Qd"))
    table = (Card("Qc"), Card("Qh"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_K():
    hand = (Card("Ks"), Card("Kd"))
    table = (Card("Kc"), Card("Kh"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8


def test_four_of_a_kind_A():
    hand = (Card("As"), Card("Ad"))
    table = (Card("Ac"), Card("Ah"), )
    game = PokerGame(hand, table)
    assert game.determine_hand() == 8
