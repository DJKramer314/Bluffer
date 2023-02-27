from card import Card


class PokerGame:
    def __init__(self,
                 hand: tuple[Card],
                 table: tuple[Card] = ()):
        self.hand = hand
        # Table is an optional input, as the table may not have any cards
        self.table = table
