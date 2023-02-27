class Card:

    def __str__(self):
        return f"Your card is the {self.value} of {self.suit}"

    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit