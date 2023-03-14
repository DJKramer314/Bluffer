# format:
# def test1():
#     hand = (Card("2s"), Card("3h"))
#     table = ()
#     game = PokerGame(hand, table)
#     assert game.determine_hand() == 1

f = open("generate_test_output.txt", "a")
f.truncate(0)  # This line clears the file


def generate_test(test_name: str, hand_strings: list[str, str], table_strings: list[str], expected_output: int):

    f.write(f"def {test_name}():\n")
    f.write(
        f"    hand = (Card(\"{hand_strings[0]}\"), Card(\"{hand_strings[1]}\"))\n")
    table_string = ""
    for string in table_strings:
        table_string += f"Card(\"{string}\"), "
    f.write(
        f"    table = ({table_string})\n")
    f.write("    game = PokerGame(hand, table)\n")
    f.write(f"    assert game.determine_hand() == {expected_output}\n\n")


suits = ("s", "d", "c", "h")
values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

# Royal Flush
royal_flush_card_values = values[-5::]
for suit in suits:
    generate_test(f"test_royal_flush_{suit}", [royal_flush_card_values[0]+suit, royal_flush_card_values[1]+suit], [
                  royal_flush_card_values[2]+suit, royal_flush_card_values[3]+suit, royal_flush_card_values[4]+suit], 10)

# Straight Flush
for value in range(0, 7):
    straight_flush_card_values = values[value:value+5]
    for suit in suits:
        generate_test(f"test_straight_flush_{suit}_{value+2}_to_{value+6}", [straight_flush_card_values[0]+suit, straight_flush_card_values[1]+suit], [
                      straight_flush_card_values[2]+suit, straight_flush_card_values[3]+suit, straight_flush_card_values[4]+suit], 9)

# Four of a Kind
for value in values:
    generate_test(f"test_four_of_a_kind_{value}", [value+suits[0], value+suits[1]], [
        value+suits[2], value+suits[3]], 8)
