from card import Card


class PokerGame:
    # Table is initialized as an optional input because the table may not have any cards, in which it will be initialized as an empty tuple
    def __init__(self,
                 hand: tuple[Card],
                 table: tuple[Card] = ()):
        self.hand = hand
        self.table = table

        self.deck = self.create_deck()

    def create_deck(self):
        deck: list[Card] = []
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        return deck

    def calculate_winning_odds(self) -> float:
        return 1.0
