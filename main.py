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


hand = get_user_hand()
for card in hand:
    print(card)
