from card import Card


class PokerGame:

    def __init__(self,
                 hand: tuple[Card],
                 table: tuple[Card] = ()):
        """
        This init constructor takes in two arguments, a 'hand' and a 'table.'
        The 'hand' object is assumed to be a tuple[Card] of length 2.
        The 'table' object is assumed to be a tuple[Card] of any length between 0 and 5 inclusive.
        """
        self.hand = hand
        self.table = table

        self.deck = self.create_deck()

    def create_deck(self) -> tuple[Card]:
        """
        This method creates a default deck of 52 cards.
        This deck is unshuffled and the method simply returns a tuple[Card]
        """
        deck: list[Card] = []
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        # The values above 10 are face cards and Ace
        values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        return tuple(deck)

    def calculate_winning_odds(self) -> float:
        return 1.0
