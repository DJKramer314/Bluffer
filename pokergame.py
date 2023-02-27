from card import Card


class PokerGame:
    # Table is initialized as an optional input because the table may not have any cards, in which it will be initialized as an empty tuple
    def __init__(self,
                 hand: tuple[Card],
                 table: tuple[Card] = ()):
        self.hand = hand
        self.table = table

    def calculate_winning_odds(self) -> float:
        return 1.0
