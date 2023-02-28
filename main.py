from pokergame import PokerGame
from card import Card


def get_user_hand():
    user_string = input("Enter your hand: ")
    card_strings = user_string.split(" ")
    if len(card_strings) == 2:
        pass
    else:
        print(
            f"Wrong number of inputs. Expected 2, but received {len(card_strings)}.")
        # Repeat through recursion
        return get_user_hand()

    try:
        card_one = Card(card_strings[0])
        card_two = Card(card_strings[1])
    except:
        print("Invalid input(s). Please try again")
        # Repeat through recursion
        return get_user_hand()

    return (card_one, card_two)


def get_table_cards():
    table_string = input("Enter table cards: ")

    if table_string == "":
        return ()

    card_strings = table_string.split(" ")
    if len(card_strings) < 5:
        pass
    else:
        print(
            f"Too many inputs. Expected 5 or less, but received {len(card_strings)}.")
        # Repeat through recursion
        return get_table_cards()
    cards = []
    try:
        for card_string in card_strings:
            cards.append(Card(card_string))
        else:
            pass
    except:
        print("Invalid input(s). Please try again")
        # Repeat through recursion
        return get_table_cards()

    return tuple(cards)


hand = get_user_hand()
table = get_table_cards()

game = PokerGame(hand, table)