class Card:

    def __str__(self):
        # This variable is either a number (2-10) or a full name of a card, such as 'King'
        name: str

        # This conditional is for special names for the face cards and Ace
        if self.value > 10:
            name_values = {
                "11": "Jack",
                "12": "Queen",
                "13": "King",
                "14": "Ace"
            }
            name = name_values[str(self.value)]
        else:
            name = str(self.value)
        return f"The {name} of {self.suit}"

    # None is specified here to allow for an optional constructor argument
    def __init__(self, string: str, value: int = None):

        if value:
            # This only occurs if a card string and value is specified in the constructor
            # While a string may also include a value, it is not known until the else statement
            # This process, while slightly hard to read, is the only way that I can overload the constructor
            self.value = value
            self.suit = string

        else:
            # This spot is only reached when a string and not a value is specified in the constructor
            # The string must be in the format "AB" where A = 2-10 or J Q K, and B = s, c, h, or d for the suit
            formatted_input = self.format_input(string)
            self.value, self.suit = formatted_input[0], formatted_input[1]

    def format_input(self, input: str) -> tuple:
        value: int = input[0:-1]  # A number (2-10) or a letter (A, K, Q, J)
        suit: str = input[-1]  # A letter (s, c, h, d)

        value_dictionary = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }

        suit_dictionary = {
            "s": "Spades",
            "c": "Clubs",
            "h": "Hearts",
            "d": "Diamonds"
        }

        return (value_dictionary[value], suit_dictionary[suit])
