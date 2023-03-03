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


def generate_hand_values_with_no_pairs_or_straights() -> set[set[int]]:
    hands_list = set()
    for value1 in range(2, 15):
        for value2 in range(2, 15):
            for value3 in range(2, 15):
                for value4 in range(2, 15):
                    for value5 in range(2, 15):
                        for value6 in range(2, 15):
                            for value7 in range(2, 15):
                                value_list = [value1, value2, value3,
                                              value4, value5, value6, value7]
                                if len(value_list) == len(set(value_list)):
                                    # No pairs exist
                                    straight_set = set(value_list)

                                    straight_sets = (
                                        {14, 2, 3, 4, 5},
                                        {2, 3, 4, 5, 6},
                                        {3, 4, 5, 6, 7},
                                        {4, 5, 6, 7, 8},
                                        {5, 6, 7, 8, 9},
                                        {6, 7, 8, 9, 10},
                                        {7, 8, 9, 10, 11},
                                        {8, 9, 10, 11, 12},
                                        {9, 10, 11, 12, 13},
                                        {10, 11, 12, 13, 14},
                                    )

                                    has_straight = False
                                    for straight in straight_sets:
                                        if len(straight_set.intersection(straight)) == 5:
                                            has_straight = True
                                    if not has_straight:
                                        hands_list.add(frozenset(value_list))
    return hands_list


hands_list = generate_hand_values_with_no_pairs_or_straights()
for hand in list[hands_list]:
    print(hand)
