from card import Card


class PokerGame:

    """
    The PokerGame class is designed to keep all of the data related to a game of poker. It can
    store a player's hand, the table's cards, and the deck of cards as a whole. This app is designed to calculate the odds from
    a single player's perspective, but will be allowed in the future to calculate given multiple hands.
    """

    def __str__(self):
        return_string = "Cards in your hand: \n"
        for card in self.hand:
            return_string += " - " + str(card) + "\n"
        return_string += "Cards on the table: \n"
        for card in self.table:
            return_string += " - " + str(card) + "\n"
        return_string += f"Number of players: {self.number_of_players}"
        return return_string

    def __init__(self,
                 hand: tuple[Card],
                 table: tuple[Card],
                 number_of_players: int):
        """
        This init constructor takes in two arguments, a 'hand' and a 'table.'
        The 'hand' object is assumed to be a tuple[Card] of length 2.
        The 'table' object is assumed to be a tuple[Card] of any length between 0 and 5 inclusive.
        """
        self.hand = hand
        self.table = table
        self.number_of_players = number_of_players

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
