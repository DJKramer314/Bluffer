class Card:

    def __str__(self):
        return f"The {self.value} of {self.suit}"

    def __init__(self, string: str, value: int = None):

        if value:
            # This only occurs if a card value is specified in the initialization of the Card object
            # While a string may also include a value, it is not known until the else statement
            # This method, while slightly hard to read, is the only way that I can overload the constructor
            self.value = value
            self.suit = string

        else:
            # This spot is reached when only a string is specified in the constructor
            # The string must be in the format "AB" where A = 2-10 or J Q K, and B = s, c, h, or d for the suit
            suit_string = ""

            # This check is necessary to ensure that a 10 is not mistaken for a 1
            # It is not more efficient to use negative indexing because we would still have to check if there are 3 characters
            if string[0:2] == "10":
                self.value = 10
                suit_string = string[2]
            else:
                self.value = string[0]
                suit_string = string[1]

            suit_values = {
                "s": "Spades",
                "c": "Clubs",
                "h": "Hearts",
                "d": "Diamonds"
            }

            self.suit = suit_values[suit_string]
