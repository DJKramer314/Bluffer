from card import Card
from hand import Hand


class PokerGame:

    def __init__(self,
                 hand: Hand,
                 table: tuple(Card) = ()):
        self.hand = hand
        # Table is an optional input, as the table may not have any cards
        self.table = table
