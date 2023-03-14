# format:
# def test1():
#     hand = (Card("2s"), Card("3h"))
#     table = ()
#     game = PokerGame(hand, table)
#     assert game.determine_hand() == 1

def generate_test(test_name: str, hand_strings: list[str, str], table_strings: list[str], expected_output: int):
    print(f"def {test_name}():")
    print(
        f"    hand = (Card(\"{hand_strings[0]}\"), Card(\"{hand_strings[1]}\"))")
    table_string = ""
    for string in table_strings:
        table_string += f"Card(\"{string}\"), "
    print(
        f"    table = ({table_string})")
    print("    game = PokerGame(hand, table)")
    print(f"    assert game.determine_hand() == {expected_output}")


generate_test("test1", ["2s", "2s"], ["2h", "As"], 2)
