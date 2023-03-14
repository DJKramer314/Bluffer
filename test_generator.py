# format:
# def test1():
#     hand = (Card("2s"), Card("3h"))
#     table = ()
#     game = PokerGame(hand, table)
#     assert game.determine_hand() == 1

def generate_test(test_name: str, hand_strings: list[str, str], table_strings: list[str], expected_output: int):
    f = open("generate_test_output.txt", "a")
    f.write(f"def {test_name}():\n")
    f.write(
        f"    hand = (Card(\"{hand_strings[0]}\"), Card(\"{hand_strings[1]}\"))\n")
    table_string = ""
    for string in table_strings:
        table_string += f"Card(\"{string}\"), "
    f.write(
        f"    table = ({table_string})\n")
    f.write("    game = PokerGame(hand, table)\n")
    f.write(f"    assert game.determine_hand() == {expected_output}\n")
